try:
    from time import ticks_us, ticks_diff
except ImportError:
    from time import time_ns

    def ticks_us(): return int(time_ns() * 1000)
    def ticks_diff(a, b): return a - b

class RandomForestClassifier:
    """
    # RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_name=RandomForestClassifier, class_weight=None, criterion=gini, estimator=DecisionTreeClassifier(), estimator_params=('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha', 'monotonic_cst'), max_depth=None, max_features=sqrt, max_leaf_nodes=16, max_samples=None, min_impurity_decrease=0.0, min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0, monotonic_cst=None, n_estimators=16, n_jobs=None, num_outputs=10, oob_score=False, package_name=everywhereml.sklearn.ensemble, random_state=None, template_folder=everywhereml/sklearn/ensemble, verbose=0, warm_start=False)
    """

    def __init__(self):
        """
        Constructor
        """
        self.latency = 0
        self.predicted_value = -1

        self.votes = [0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000]

    def predict(self, x):
        """
        Predict output from input vector
        """
        self.predicted_value = -1
        started_at = ticks_us()

        self.votes = [0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000]

        idx, score = self.tree0(x)
        self.votes[idx] += score
        
        idx, score = self.tree1(x)
        self.votes[idx] += score
        
        idx, score = self.tree2(x)
        self.votes[idx] += score
        
        idx, score = self.tree3(x)
        self.votes[idx] += score
        
        idx, score = self.tree4(x)
        self.votes[idx] += score
        
        idx, score = self.tree5(x)
        self.votes[idx] += score
        
        idx, score = self.tree6(x)
        self.votes[idx] += score
        
        idx, score = self.tree7(x)
        self.votes[idx] += score
        
        idx, score = self.tree8(x)
        self.votes[idx] += score
        
        idx, score = self.tree9(x)
        self.votes[idx] += score
        
        idx, score = self.tree10(x)
        self.votes[idx] += score
        
        idx, score = self.tree11(x)
        self.votes[idx] += score
        
        idx, score = self.tree12(x)
        self.votes[idx] += score
        
        idx, score = self.tree13(x)
        self.votes[idx] += score
        
        idx, score = self.tree14(x)
        self.votes[idx] += score
        
        idx, score = self.tree15(x)
        self.votes[idx] += score

        # get argmax of votes
        max_vote = max(self.votes)
        self.predicted_value = next(i for i, v in enumerate(self.votes) if v == max_vote)

        self.latency = ticks_diff(ticks_us(), started_at)
        return self.predicted_value

    def latencyInMicros(self):
        """
        Get latency in micros
        """
        return self.latency

    def latencyInMillis(self):
        """
        Get latency in millis
        """
        return self.latency // 1000

    def tree0(self, x):
        """
        Random forest's tree #0
        """
        if x[51] < -17.374418258666992:
            if x[85] < 0.4369506984949112:
                return 0, 0.07670454545454546
            else:
                return 3, 0.13068181818181818
        else:
            if x[83] < -12.354906558990479:
                if x[54] < 0.8348746597766876:
                    return 8, 0.10511363636363637
                else:
                    return 0, 0.07670454545454546
            else:
                if x[38] < -0.07726983726024628:
                    return 5, 0.08522727272727272
                else:
                    if x[81] < -16.204832077026367:
                        if x[34] < -1.0000812113285065:
                            return 1, 0.09943181818181818
                        else:
                            return 2, 0.10227272727272728
                    else:
                        if x[80] < -0.04115241579711437:
                            return 7, 0.09375
                        else:
                            if x[108] < 0.7910156548023224:
                                if x[42] < 0.8613905310630798:
                                    return 4, 0.125
                                else:
                                    return 9, 0.09659090909090909
                            else:
                                if x[72] < 0.8883309066295624:
                                    if x[12] < 0.8252545893192291:
                                        return 6, 0.08522727272727272
                                    else:
                                        return 1, 0.09943181818181818
                                else:
                                    if x[42] < 0.930177628993988:
                                        if x[68] < 0.12801369652152061:
                                            return 4, 0.125
                                        else:
                                            if x[73] < 0.3536030948162079:
                                                return 4, 0.125
                                            else:
                                                return 6, 0.08522727272727272
                                    else:
                                        return 0, 0.07670454545454546

    def tree1(self, x):
        """
        Random forest's tree #1
        """
        if x[38] < -0.04304404743015766:
            if x[51] < -17.374418258666992:
                return 3, 0.08806818181818182
            else:
                return 5, 0.13352272727272727
        else:
            if x[25] < 0.3782840818166733:
                if x[97] < 0.5219902098178864:
                    if x[15] < -24.42802333831787:
                        return 8, 0.08522727272727272
                    else:
                        return 0, 0.11647727272727272
                else:
                    return 9, 0.12215909090909091
            else:
                if x[71] < 5.264281988143921:
                    if x[94] < -6.692192316055298:
                        if x[89] < 10.066367626190186:
                            if x[72] < 0.6980591118335724:
                                return 8, 0.08522727272727272
                            else:
                                return 2, 0.09659090909090909
                        else:
                            return 4, 0.08522727272727272
                    else:
                        if x[30] < 0.7809531688690186:
                            return 6, 0.08522727272727272
                        else:
                            if x[56] < -0.028586622327566147:
                                return 8, 0.08522727272727272
                            else:
                                if x[38] < 0.19317398965358734:
                                    return 1, 0.08238636363636363
                                else:
                                    return 6, 0.08522727272727272
                else:
                    if x[10] < -6.32666015625:
                        if x[30] < 0.8627506196498871:
                            return 4, 0.08522727272727272
                        else:
                            return 9, 0.12215909090909091
                    else:
                        if x[86] < 0.06266123056411743:
                            return 7, 0.10511363636363637
                        else:
                            return 9, 0.12215909090909091

    def tree2(self, x):
        """
        Random forest's tree #2
        """
        if x[19] < 0.36202099919319153:
            return 0, 0.11647727272727272
        else:
            if x[66] < 0.8618662059307098:
                if x[82] < -7.954419851303101:
                    if x[93] < -2.8799875378608704:
                        if x[101] < -17.071450233459473:
                            return 8, 0.09375
                        else:
                            return 2, 0.09659090909090909
                    else:
                        return 8, 0.09375
                else:
                    if x[74] < 0.04986572265625:
                        return 7, 0.13636363636363635
                    else:
                        if x[84] < 0.7908950746059418:
                            return 9, 0.09375
                        else:
                            if x[42] < 0.7920013964176178:
                                return 6, 0.07954545454545454
                            else:
                                return 1, 0.09659090909090909
            else:
                if x[56] < -0.037266816943883896:
                    return 5, 0.10511363636363637
                else:
                    if x[16] < 10.94274091720581:
                        if x[24] < 0.7674687802791595:
                            if x[44] < -0.05328625440597534:
                                return 3, 0.09659090909090909
                            else:
                                return 6, 0.07954545454545454
                        else:
                            if x[6] < 0.8419728577136993:
                                return 4, 0.08522727272727272
                            else:
                                if x[117] < 3.5823776721954346:
                                    if x[116] < 0.04888915829360485:
                                        return 5, 0.10511363636363637
                                    else:
                                        return 1, 0.09659090909090909
                                else:
                                    return 9, 0.09375
                    else:
                        return 3, 0.09659090909090909

    def tree3(self, x):
        """
        Random forest's tree #3
        """
        if x[28] < -13.698716640472412:
            if x[71] < 0.33646439760923386:
                return 6, 0.14772727272727273
            else:
                return 4, 0.06818181818181818
        else:
            if x[83] < -10.086059093475342:
                if x[1] < 0.4024432897567749:
                    return 0, 0.09943181818181818
                else:
                    return 8, 0.10511363636363637
            else:
                if x[116] < -0.040086451917886734:
                    if x[72] < 0.8414713442325592:
                        if x[60] < 0.8416133522987366:
                            return 7, 0.11363636363636363
                        else:
                            return 9, 0.09090909090909091
                    else:
                        if x[6] < 0.881216824054718:
                            if x[102] < 0.845043271780014:
                                return 5, 0.08522727272727272
                            else:
                                return 1, 0.11931818181818182
                        else:
                            return 3, 0.09659090909090909
                else:
                    if x[85] < 0.4014212489128113:
                        if x[36] < 0.8275757133960724:
                            return 6, 0.14772727272727273
                        else:
                            return 0, 0.09943181818181818
                    else:
                        if x[33] < 2.481040835380554:
                            if x[57] < 2.863054037094116:
                                if x[30] < 0.7691528797149658:
                                    return 4, 0.06818181818181818
                                else:
                                    return 1, 0.11931818181818182
                            else:
                                return 4, 0.06818181818181818
                        else:
                            if x[88] < -19.927974700927734:
                                return 2, 0.07386363636363637
                            else:
                                return 3, 0.09659090909090909

    def tree4(self, x):
        """
        Random forest's tree #4
        """
        if x[25] < 0.32883942127227783:
            return 0, 0.10227272727272728
        else:
            if x[82] < -12.039586067199707:
                if x[24] < 0.8962190449237823:
                    if x[83] < 10.869279861450195:
                        if x[33] < 28.73121452331543:
                            if x[77] < -13.18984317779541:
                                return 8, 0.10795454545454546
                            else:
                                return 2, 0.12215909090909091
                        else:
                            return 8, 0.10795454545454546
                    else:
                        return 4, 0.07670454545454546
                else:
                    return 8, 0.10795454545454546
            else:
                if x[65] < -5.015191078186035:
                    if x[70] < -1.8045295476913452:
                        return 2, 0.12215909090909091
                    else:
                        return 6, 0.13068181818181818
                else:
                    if x[27] < -13.007270812988281:
                        if x[84] < 0.833633542060852:
                            return 9, 0.11363636363636363
                        else:
                            return 4, 0.07670454545454546
                    else:
                        if x[70] < 3.58734130859375:
                            if x[36] < 0.8074942827224731:
                                if x[95] < 8.405737400054932:
                                    return 5, 0.06818181818181818
                                else:
                                    if x[41] < -2.427056074142456:
                                        return 3, 0.09943181818181818
                                    else:
                                        return 5, 0.06818181818181818
                            else:
                                if x[21] < 3.7979131937026978:
                                    return 1, 0.09659090909090909
                                else:
                                    return 3, 0.09943181818181818
                        else:
                            return 7, 0.08238636363636363

    def tree5(self, x):
        """
        Random forest's tree #5
        """
        if x[37] < 0.4294024854898453:
            if x[2] < -0.02916768752038479:
                return 9, 0.11931818181818182
            else:
                if x[32] < 0.29496097564697266:
                    if x[31] < 0.5149610936641693:
                        return 0, 0.1534090909090909
                    else:
                        return 7, 0.09375
                else:
                    return 4, 0.09943181818181818
        else:
            if x[72] < 0.819789856672287:
                if x[89] < -11.010005474090576:
                    return 8, 0.07102272727272728
                else:
                    if x[33] < -8.987425804138184:
                        return 9, 0.11931818181818182
                    else:
                        if x[76] < 2.0359475016593933:
                            return 2, 0.08238636363636363
                        else:
                            return 7, 0.09375
            else:
                if x[76] < 9.545667171478271:
                    if x[30] < 0.8511855602264404:
                        if x[68] < 0.03513054735958576:
                            if x[64] < -7.027147531509399:
                                return 5, 0.08522727272727272
                            else:
                                return 2, 0.08238636363636363
                        else:
                            if x[54] < 0.8931297957897186:
                                if x[17] < -0.6336692497134209:
                                    return 4, 0.09943181818181818
                                else:
                                    return 3, 0.07954545454545454
                            else:
                                return 3, 0.07954545454545454
                    else:
                        if x[6] < 0.8428065180778503:
                            return 4, 0.09943181818181818
                        else:
                            return 1, 0.11079545454545454
                else:
                    return 6, 0.10511363636363637

    def tree6(self, x):
        """
        Random forest's tree #6
        """
        if x[41] < 5.101225852966309:
            if x[79] < 0.344783291220665:
                return 0, 0.09375
            else:
                if x[38] < 0.26474855840206146:
                    if x[24] < 0.7670166194438934:
                        if x[65] < 1.0845817923545837:
                            return 6, 0.11079545454545454
                        else:
                            return 3, 0.10227272727272728
                    else:
                        if x[95] < 1.6030919551849365:
                            if x[69] < -12.495935440063477:
                                return 2, 0.11931818181818182
                            else:
                                return 1, 0.08238636363636363
                        else:
                            if x[77] < -1.2393298894166946:
                                return 2, 0.11931818181818182
                            else:
                                if x[18] < 0.8436761498451233:
                                    return 3, 0.10227272727272728
                                else:
                                    return 5, 0.08806818181818182
                else:
                    return 4, 0.08806818181818182
        else:
            if x[76] < -2.4626888632774353:
                if x[41] < 12.422221660614014:
                    return 2, 0.11931818181818182
                else:
                    if x[64] < -26.70876407623291:
                        return 3, 0.10227272727272728
                    else:
                        return 8, 0.08806818181818182
            else:
                if x[27] < -13.007270812988281:
                    return 9, 0.11647727272727272
                else:
                    if x[86] < 0.0611010417342186:
                        return 7, 0.11079545454545454
                    else:
                        if x[7] < 0.39953678846359253:
                            return 0, 0.09375
                        else:
                            return 2, 0.11931818181818182

    def tree7(self, x):
        """
        Random forest's tree #7
        """
        if x[30] < 0.8519745767116547:
            if x[18] < 0.8039093911647797:
                if x[59] < -0.19016222655773163:
                    if x[71] < 0.33646439760923386:
                        return 6, 0.15056818181818182
                    else:
                        return 4, 0.06818181818181818
                else:
                    return 3, 0.08238636363636363
            else:
                if x[28] < 6.139639854431152:
                    if x[32] < 0.04135388694703579:
                        return 5, 0.11647727272727272
                    else:
                        return 7, 0.11647727272727272
                else:
                    if x[46] < -10.519920349121094:
                        return 3, 0.08238636363636363
                    else:
                        if x[14] < 0.1858191415667534:
                            return 2, 0.08806818181818182
                        else:
                            return 2, 0.08806818181818182
        else:
            if x[15] < -15.847779273986816:
                if x[39] < -2.665817379951477:
                    if x[76] < 2.7038573026657104:
                        return 4, 0.06818181818181818
                    else:
                        return 9, 0.10511363636363637
                else:
                    if x[30] < 0.8838774561882019:
                        return 4, 0.06818181818181818
                    else:
                        return 8, 0.08806818181818182
            else:
                if x[25] < 0.39409179985523224:
                    return 0, 0.09943181818181818
                else:
                    if x[40] < 4.184070706367493:
                        if x[0] < 0.8312771916389465:
                            return 9, 0.10511363636363637
                        else:
                            return 1, 0.08522727272727272
                    else:
                        return 7, 0.11647727272727272

    def tree8(self, x):
        """
        Random forest's tree #8
        """
        if x[12] < 0.9292132258415222:
            if x[94] < -4.154116868972778:
                if x[34] < 2.7019468545913696:
                    if x[66] < 0.8113762140274048:
                        return 7, 0.08806818181818182
                    else:
                        return 4, 0.06818181818181818
                else:
                    return 2, 0.11647727272727272
            else:
                if x[51] < -16.741125106811523:
                    if x[38] < -0.022705078125:
                        return 3, 0.09659090909090909
                    else:
                        if x[24] < 0.7550796270370483:
                            return 6, 0.13352272727272727
                        else:
                            return 0, 0.09090909090909091
                else:
                    if x[36] < 0.825312465429306:
                        if x[62] < 0.10822779685258865:
                            if x[55] < 0.6106096506118774:
                                return 5, 0.08238636363636363
                            else:
                                return 6, 0.13352272727272727
                        else:
                            return 6, 0.13352272727272727
                    else:
                        if x[40] < 3.349130153656006:
                            if x[33] < -12.8489408493042:
                                return 9, 0.10227272727272728
                            else:
                                if x[81] < 4.391467928886414:
                                    return 1, 0.10795454545454546
                                else:
                                    return 6, 0.13352272727272727
                        else:
                            return 7, 0.08806818181818182
        else:
            if x[61] < 0.5870315134525299:
                if x[108] < 0.8723840415477753:
                    return 9, 0.10227272727272728
                else:
                    return 0, 0.09090909090909091
            else:
                return 8, 0.11363636363636363

    def tree9(self, x):
        """
        Random forest's tree #9
        """
        if x[53] < 7.409978628158569:
            if x[87] < -16.99389362335205:
                if x[65] < -3.193709135055542:
                    return 2, 0.12215909090909091
                else:
                    return 1, 0.09090909090909091
            else:
                if x[28] < -10.404025554656982:
                    if x[88] < -4.9421775341033936:
                        return 4, 0.07670454545454546
                    else:
                        if x[89] < 10.420601844787598:
                            return 6, 0.13920454545454544
                        else:
                            return 3, 0.07102272727272728
                else:
                    if x[62] < -0.03478558361530304:
                        return 5, 0.07670454545454546
                    else:
                        if x[13] < 0.3617858737707138:
                            return 0, 0.09943181818181818
                        else:
                            if x[28] < 6.427001476287842:
                                if x[89] < 2.4703131914138794:
                                    return 1, 0.09090909090909091
                                else:
                                    return 0, 0.09943181818181818
                            else:
                                if x[89] < 3.684756278991699:
                                    return 2, 0.12215909090909091
                                else:
                                    return 3, 0.07102272727272728
        else:
            if x[74] < 0.0389113649725914:
                if x[82] < -7.494025230407715:
                    return 8, 0.11363636363636363
                else:
                    return 7, 0.10511363636363637
            else:
                if x[114] < 0.882432758808136:
                    return 9, 0.10511363636363637
                else:
                    if x[69] < -8.991231679916382:
                        return 8, 0.11363636363636363
                    else:
                        return 0, 0.09943181818181818

    def tree10(self, x):
        """
        Random forest's tree #10
        """
        if x[42] < 0.897355854511261:
            if x[66] < 0.8581321835517883:
                if x[88] < -26.296338081359863:
                    return 2, 0.10227272727272728
                else:
                    if x[83] < -9.20867919921875:
                        return 8, 0.10227272727272728
                    else:
                        if x[47] < 8.70513916015625:
                            if x[36] < 0.7842085063457489:
                                return 2, 0.10227272727272728
                            else:
                                return 1, 0.08238636363636363
                        else:
                            if x[73] < 0.8004760444164276:
                                if x[46] < 0.7166589945554733:
                                    return 9, 0.10511363636363637
                                else:
                                    return 7, 0.09943181818181818
                            else:
                                return 8, 0.10227272727272728
            else:
                if x[82] < 15.284075736999512:
                    if x[22] < -7.23174524307251:
                        if x[96] < 0.931374728679657:
                            return 4, 0.08806818181818182
                        else:
                            return 6, 0.11931818181818182
                    else:
                        if x[68] < -0.0032966788858175278:
                            return 5, 0.06534090909090909
                        else:
                            if x[105] < -8.590700149536133:
                                return 1, 0.08238636363636363
                            else:
                                return 3, 0.13068181818181818
                else:
                    return 6, 0.11931818181818182
        else:
            if x[90] < 0.8674733936786652:
                if x[26] < -0.18803712725639343:
                    return 3, 0.13068181818181818
                else:
                    return 9, 0.10511363636363637
            else:
                return 0, 0.10511363636363637

    def tree11(self, x):
        """
        Random forest's tree #11
        """
        if x[12] < 0.9244493842124939:
            if x[33] < -10.093691349029541:
                if x[65] < -5.577479362487793:
                    return 6, 0.11647727272727272
                else:
                    if x[94] < 0.9866907894611359:
                        return 4, 0.09943181818181818
                    else:
                        if x[52] < -5.666521787643433:
                            return 3, 0.08806818181818182
                        else:
                            return 9, 0.10511363636363637
            else:
                if x[82] < -9.098551511764526:
                    return 2, 0.09943181818181818
                else:
                    if x[46] < 6.026331186294556:
                        if x[30] < 0.84490966796875:
                            if x[74] < 0.1456068977713585:
                                if x[66] < 0.8606333434581757:
                                    return 1, 0.09943181818181818
                                else:
                                    return 5, 0.07954545454545454
                            else:
                                if x[28] < -14.883652210235596:
                                    return 6, 0.11647727272727272
                                else:
                                    if x[11] < 14.106785297393799:
                                        return 3, 0.08806818181818182
                                    else:
                                        return 2, 0.09943181818181818
                        else:
                            return 1, 0.09943181818181818
                    else:
                        return 7, 0.09375
        else:
            if x[13] < 0.3803711086511612:
                if x[48] < 0.8374713659286499:
                    return 8, 0.10795454545454546
                else:
                    return 0, 0.11079545454545454
            else:
                if x[71] < 14.424915313720703:
                    return 8, 0.10795454545454546
                else:
                    return 9, 0.10511363636363637

    def tree12(self, x):
        """
        Random forest's tree #12
        """
        if x[13] < 0.3599853515625:
            return 0, 0.09375
        else:
            if x[53] < 7.518198490142822:
                if x[34] < -5.020141124725342:
                    if x[100] < 1.3081609606742859:
                        return 4, 0.09375
                    else:
                        if x[57] < -20.716659545898438:
                            return 3, 0.09375
                        else:
                            return 6, 0.13636363636363635
                else:
                    if x[82] < -18.443150520324707:
                        return 2, 0.09659090909090909
                    else:
                        if x[33] < 4.611840486526489:
                            if x[89] < 3.7731584310531616:
                                return 1, 0.07386363636363637
                            else:
                                if x[51] < 2.088084042072296:
                                    return 5, 0.0625
                                else:
                                    return 4, 0.09375
                        else:
                            if x[73] < 0.47113753855228424:
                                return 3, 0.09375
                            else:
                                return 2, 0.09659090909090909
            else:
                if x[2] < -0.08687205612659454:
                    if x[62] < 0.057608483359217644:
                        return 8, 0.11363636363636363
                    else:
                        if x[110] < 0.13509652018547058:
                            return 9, 0.13068181818181818
                        else:
                            return 8, 0.11363636363636363
                else:
                    if x[51] < -0.11242697946727276:
                        return 9, 0.13068181818181818
                    else:
                        if x[84] < 0.8220085799694061:
                            return 7, 0.10511363636363637
                        else:
                            return 8, 0.11363636363636363

    def tree13(self, x):
        """
        Random forest's tree #13
        """
        if x[77] < -0.015072131529450417:
            if x[40] < 17.156982421875:
                if x[18] < 0.8093928396701813:
                    return 6, 0.10227272727272728
                else:
                    if x[39] < -0.6958007216453552:
                        return 1, 0.11363636363636363
                    else:
                        if x[89] < -11.8703932762146:
                            return 0, 0.09090909090909091
                        else:
                            return 2, 0.09659090909090909
            else:
                if x[83] < -9.119190692901611:
                    return 8, 0.10511363636363637
                else:
                    return 2, 0.09659090909090909
        else:
            if x[44] < -0.05892549455165863:
                if x[57] < -10.97896432876587:
                    return 3, 0.09659090909090909
                else:
                    return 5, 0.11931818181818182
            else:
                if x[76] < 12.20026969909668:
                    if x[27] < 2.234230160713196:
                        if x[102] < 0.922080397605896:
                            if x[16] < -10.260011196136475:
                                if x[72] < 0.8974734842777252:
                                    return 3, 0.09659090909090909
                                else:
                                    return 4, 0.056818181818181816
                            else:
                                return 1, 0.11363636363636363
                        else:
                            return 0, 0.09090909090909091
                    else:
                        return 7, 0.10511363636363637
                else:
                    if x[27] < -13.318549633026123:
                        return 9, 0.11363636363636363
                    else:
                        if x[52] < 5.563693016767502:
                            return 6, 0.10227272727272728
                        else:
                            return 7, 0.10511363636363637

    def tree14(self, x):
        """
        Random forest's tree #14
        """
        if x[45] < 2.6473993062973022:
            if x[15] < -21.470303535461426:
                return 9, 0.10795454545454546
            else:
                if x[28] < -13.300397396087646:
                    if x[89] < 9.95039987564087:
                        return 6, 0.11363636363636363
                    else:
                        return 4, 0.07954545454545454
                else:
                    if x[36] < 0.8255053162574768:
                        if x[74] < 0.14776310324668884:
                            return 5, 0.10511363636363637
                        else:
                            return 3, 0.09659090909090909
                    else:
                        if x[97] < 0.42158450186252594:
                            return 0, 0.08806818181818182
                        else:
                            if x[89] < 3.332519292831421:
                                return 1, 0.09943181818181818
                            else:
                                if x[8] < 0.05500391498208046:
                                    return 9, 0.10795454545454546
                                else:
                                    return 3, 0.09659090909090909
        else:
            if x[60] < 0.7031121253967285:
                return 8, 0.10511363636363637
            else:
                if x[81] < -16.998290061950684:
                    return 2, 0.08806818181818182
                else:
                    if x[15] < 0.8027550280094147:
                        if x[77] < 7.4003214836120605:
                            if x[19] < 0.33979471027851105:
                                return 0, 0.08806818181818182
                            else:
                                return 6, 0.11363636363636363
                        else:
                            return 4, 0.07954545454545454
                    else:
                        if x[61] < 0.7034912407398224:
                            return 7, 0.11647727272727272
                        else:
                            return 2, 0.08806818181818182

    def tree15(self, x):
        """
        Random forest's tree #15
        """
        if x[73] < 0.22207077592611313:
            return 0, 0.11079545454545454
        else:
            if x[72] < 0.8488551378250122:
                if x[82] < -1.2153891623020172:
                    if x[15] < -17.44359016418457:
                        return 8, 0.09659090909090909
                    else:
                        return 2, 0.09090909090909091
                else:
                    if x[33] < -4.422531723976135:
                        return 9, 0.11363636363636363
                    else:
                        if x[70] < 1.4947585314512253:
                            return 1, 0.08806818181818182
                        else:
                            return 7, 0.10227272727272728
            else:
                if x[38] < 0.3173217475414276:
                    if x[27] < 9.94078779220581:
                        if x[64] < -6.548904657363892:
                            if x[110] < -0.11903918534517288:
                                if x[42] < 0.835545688867569:
                                    return 5, 0.10511363636363637
                                else:
                                    return 3, 0.11363636363636363
                            else:
                                return 3, 0.11363636363636363
                        else:
                            if x[6] < 0.8206096887588501:
                                if x[83] < 5.657957434654236:
                                    return 6, 0.07954545454545454
                                else:
                                    return 4, 0.09943181818181818
                            else:
                                if x[76] < 6.826672554016113:
                                    return 1, 0.08806818181818182
                                else:
                                    if x[1] < 0.5439029335975647:
                                        return 0, 0.11079545454545454
                                    else:
                                        return 9, 0.11363636363636363
                    else:
                        return 3, 0.11363636363636363
                else:
                    return 4, 0.09943181818181818