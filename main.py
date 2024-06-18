import time
from time import sleep
from lsm6dsox import LSM6DSOX
import ssd1306
from machine import Pin, I2C, SoftI2C, ADC, Pin
from MyModel import RandomForestClassifier


# Initialize I2C interface for OLED
i2c = SoftI2C(scl=Pin(13), sda=Pin(12))
# Initialize SSD1306 OLED display
oled_width = 128
oled_height = 32  # Adjusted for 128x32 OLED display
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Scan for I2C devices
devices = i2c.scan()
if not devices:
    raise RuntimeError('No I2C devices found')
else:
    print('I2C devices found:', devices)
    
def write_display(*txt_rows):
    oled.fill(0)  # Clear the display
    for i, txt in enumerate(txt_rows):
        oled.text(txt, 0, i * 10)
    oled.show()  # Update the display     
    
    
# Initialize LDR sensor
analogPin = ADC(Pin(26))


# Initialize accelator and gyroscope 
lsm = LSM6DSOX(i2c)

# Initialize button key
in27 = Pin(27, Pin.IN, Pin.PULL_UP)


clf = RandomForestClassifier()


def resample_signal(signal_list, desired_length):
    def resample_channel(channel, desired_length):
        current_length = len(channel)
        if current_length == desired_length:
            return channel

        resampled_channel = []
        ratio = current_length / desired_length

        for i in range(desired_length):
            original_index = i * ratio
            index1 = int(original_index)
            index2 = min(index1 + 1, current_length - 1)
            weight = original_index - index1
            resampled_value = channel[index1] * (1 - weight) + channel[index2] * weight
            resampled_channel.append(resampled_value)

        min_original = min(channel)
        max_original = max(channel)
        min_resampled = min(resampled_channel)
        max_resampled = max(resampled_channel)
        
        if max_resampled != min_resampled:
            resampled_channel = [
                (value - min_resampled) / (max_resampled - min_resampled) * (max_original - min_original) + min_original
                for value in resampled_channel
            ]
        return resampled_channel
    transposed_signal = list(map(list, zip(*signal_list)))
    resampled_transposed_signal = [
        resample_channel(channel, desired_length) for channel in transposed_signal
    ]
    resampled_signal = list(map(list, zip(*resampled_transposed_signal)))
    return resampled_signal

write_display("Press the button to start writing")

while True:
 
    data = []
    if in27.value() == 0:
        time.sleep_ms(200)
        
        write_display("Start writing")
        while in27.value() == 0:
            acc = lsm.accel()
            gyro = lsm.gyro()
            sensor_data = [acc[0], acc[1], acc[2], gyro[0], gyro[1], gyro[2]]
            data.append(sensor_data)
            time.sleep_ms(50)
    if data != []:
        resampled = resample_signal(data, 20)
        x = [item for sublist in resampled for item in sublist]
        pred = clf.predict(x)
        write_display("The digit is : ", str(pred))
        print(pred)
        time.sleep_ms(200)

