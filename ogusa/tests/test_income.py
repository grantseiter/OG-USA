'''
Tests of income.py module
'''

import pytest
import numpy as np
from ogusa import income


def test_artctan_func():
    '''
    Test of arctan_func()
    '''
    expected_vals = np.array([0.14677821, 0.083305594, 0.057901228])
    xvals = np.array([1, 2, 3])
    a = 1.3
    b = 2.2
    c = 0.5
    test_vals = income.arctan_func(xvals, a, b, c)

    assert np.allclose(test_vals, expected_vals)


def test_artctan_deriv_func():
    '''
    Test of arctan_deriv_func()
    '''
    expected_vals = np.array([-0.109814991, -0.036400091, -0.017707961])
    xvals = np.array([1, 2, 3])
    a = 1.3
    b = 2.2
    c = 0.5
    test_vals = income.arctan_deriv_func(xvals, a, b, c)

    assert np.allclose(test_vals, expected_vals)


def test_arc_error():
    '''
    Test of arc_error()
    '''
    expected_vals = np.array([30.19765553, -1.40779391, 14.19212336])
    a = 1.3
    b = 2.2
    c = 0.5
    abc_vals = (a, b, c)
    first_point = 30.2
    coef1 = 0.05995294
    coef2 = -0.00004086
    coef3 = -0.00000521
    abil_deprec = 0.47
    params = (first_point, coef1, coef2, coef3, abil_deprec)
    test_vals = income.arc_error(abc_vals, params)

    assert np.allclose(test_vals, expected_vals)


def test_arctan_fit():
    '''
    Test arctan_fit() function
    '''
    expected_vals = np.array(
        [30.19999399, 30.19998699, 30.19997918, 30.19997039,
         30.19996043, 30.19994904, 30.1999359, 30.19992057,
         30.19990246, 30.19988072, 30.19985415, 30.19982094,
         30.19977824, 30.19972131, 30.1996416, 30.19952204, 30.19932277,
         30.19892423, 30.19772859, 14.19399974])
    a = 1.3
    b = 2.2
    c = 0.5
    init_guesses = (a, b, c)
    first_point = 30.2
    coef1 = 0.05995294
    coef2 = -0.00004086
    coef3 = -0.00000521
    abil_deprec = 0.47
    test_vals = income.arctan_fit(
        first_point, coef1, coef2, coef3, abil_deprec, init_guesses)

    assert np.allclose(test_vals, expected_vals)


def test_get_e_orig():
    '''
    Test get_e_orig() function
    '''
    expected_vals = np.array([
        [0.41637813, 0.27892939, 0.29770352, 0.34999537, 0.43550237,
         0.7104421, 1.84111771],
        [0.40966052, 0.29351488, 0.32491809, 0.38673085, 0.48142028,
         0.75826254, 1.99770813],
        [0.40406881, 0.30862551, 0.35340211, 0.42551707, 0.5298768,
         0.80925704, 2.16483317],
        [0.39951541, 0.32425432, 0.38308642, 0.46625585, 0.580742,
         0.86355704, 2.3427626],
        [0.39592303, 0.34039127, 0.41388897, 0.50882471, 0.63385587,
         0.92128697, 2.53170513],
        [0.39322307, 0.35702297, 0.44571523, 0.55307772, 0.68902964,
         0.98256181, 2.73179742],
        [0.39135441, 0.37413249, 0.47845898, 0.59884672, 0.7460476,
         1.04748443, 2.94309262],
        [0.3902622, 0.39169918, 0.51200315, 0.645943, 0.80466953,
         1.11614268, 3.16554852],
        [0.38989688, 0.40969841, 0.54622089, 0.69415939, 0.8646336,
         1.18860621, 3.39901567],
        [0.39021328, 0.42810145, 0.58097684, 0.74327267, 0.92565968,
         1.26492305, 3.64322541],
        [0.39116983, 0.44687529, 0.61612841, 0.79304632, 0.98745294,
         1.34511602, 3.89777836],
        [0.39272783, 0.46598253, 0.65152732, 0.84323347, 1.04970783,
         1.42917894, 4.16213344],
        [0.3948508, 0.48538127, 0.68702111, 0.89358009, 1.11211214,
         1.51707268, 4.43559781],
        [0.3975039, 0.50502501, 0.72245476, 0.94382825, 1.17435118,
         1.60872119, 4.71731806],
        [0.40065336, 0.52486267, 0.75767235, 0.9937194, 1.23611194,
         1.70400743, 5.00627307],
        [0.404266, 0.54483855, 0.79251866, 1.04299768, 1.29708717,
         1.80276946, 5.30126881],
        [0.40830873, 0.56489242, 0.8268408, 1.09141311, 1.35697929,
         1.90479656, 5.60093551],
        [0.41274816, 0.58495958, 0.86048981, 1.13872463, 1.41550405,
         2.00982572, 5.90372761],
        [0.41755017, 0.60497105, 0.89332205, 1.1847029, 1.47239387,
         2.11753837, 6.20792673],
        [0.42267953, 0.62485373, 0.9252007, 1.22913293, 1.5274008,
         2.22755771, 6.51164811],
        [0.42809957, 0.6445307, 0.95599693, 1.27181632, 1.58029914,
         2.33944652, 6.81285071],
        [0.4337719, 0.66392152, 0.98559107, 1.31257321, 1.63088754,
         2.45270577, 7.10935121],
        [0.43965608, 0.68294259, 1.0138736, 1.35124392, 1.6789907,
         2.56677413, 7.39884199],
        [0.44570939, 0.70150761, 1.04074596, 1.38769019, 1.72446061,
         2.68102845, 7.67891322],
        [0.45188667, 0.71952807, 1.06612125, 1.42179604, 1.76717729,
         2.79478531, 7.947079],
        [0.45814012, 0.73691379, 1.08992465, 1.45346833, 1.80704915,
         2.90730394, 8.20080721],
        [0.46441919, 0.75357353, 1.11209386, 1.4826369, 1.8440129,
         3.01779041, 8.43755302],
        [0.47067057, 0.76941566, 1.13257918, 1.50925445, 1.87803307,
         3.12540323, 8.65479541],
        [0.47683814, 0.78434886, 1.15134357, 1.5332961, 1.90910121,
         3.22926052, 8.85007629],
        [0.48286305, 0.79828285, 1.16836252, 1.5547586, 1.93723475,
         3.32844853, 9.02104147],
        [0.48868388, 0.81112921, 1.18362376, 1.57365942, 1.96247564,
         3.42203181, 9.16548263],
        [0.49423684, 0.82280213, 1.19712692, 1.59003557, 1.98488875,
         3.50906461, 9.28137951],
        [0.49945604, 0.83321932, 1.20888294, 1.60394223, 2.00456011,
         3.58860379, 9.36694123],
        [0.50427389, 0.84230278, 1.21891355, 1.61545125, 2.02159501,
         3.65972266, 9.42064568],
        [0.50862155, 0.84997968, 1.22725057, 1.62464965, 2.0361161,
         3.72152596, 9.44127599],
        [0.51242946, 0.85618315, 1.23393515, 1.63163789, 2.04826135,
         3.77316537, 9.4279529],
        [0.515628, 0.86085312, 1.23901697, 1.63652827, 2.0581821,
         3.81385546, 9.38016206],
        [0.51814816, 0.86393709, 1.24255344, 1.63944323, 2.06604115,
         3.8428897, 9.29777524],
        [0.51992236, 0.8653908, 1.24460882, 1.64051371, 2.07201085,
         3.85965604, 9.18106471],
        [0.5208853, 0.86517897, 1.24525336, 1.63987758, 2.07627136,
         3.86365177, 9.03070999],
        [0.52097488, 0.86327583, 1.24456245, 1.63767811, 2.07900905,
         3.8544972, 8.84779645],
        [0.52013315, 0.85966566, 1.24261577, 1.63406257, 2.08041495,
         3.83194769, 8.63380567],
        [0.51830734, 0.85434321, 1.23949649, 1.62918093, 2.08068349,
         3.79590369, 8.39059721],
        [0.51545085, 0.847314, 1.23529046, 1.62318461, 2.08001127,
         3.74641832, 8.12038226],
        [0.51152426, 0.83859455, 1.23008548, 1.6162255, 2.07859611,
         3.68370224, 7.82568944],
        [0.50649633, 0.82821245, 1.22397061, 1.60845493, 2.07663628,
         3.60812544, 7.50932356],
        [0.50034486, 0.81620635, 1.21703552, 1.60002298, 2.07432981,
         3.52021585, 7.17431825],
        [0.49305761, 0.80262576, 1.20936991, 1.59107771, 2.07187416,
         3.42065451, 6.82388358],
        [0.484633, 0.78753081, 1.20106298, 1.58176471, 2.06946591,
         3.31026739, 6.46135004],
        [0.47508069, 0.77099184, 1.19220294, 1.57222669, 2.06730075,
         3.19001395, 6.09011028],
        [0.46442209, 0.75308881, 1.18287666, 1.5626032, 2.0655736,
         3.06097248, 5.71356024],
        [0.45269057, 0.73391069, 1.17316925, 1.55303051, 2.06447895,
         2.92432273, 5.33504111],
        [0.43993156, 0.7135547, 1.16316384, 1.54364158, 2.06421135,
         2.78132605, 4.95778367],
        [0.4262024, 0.6921254, 1.1529413, 1.53456619, 2.0649661,
         2.63330357, 4.5848566],
        [0.41157194, 0.66973375, 1.14258011, 1.52593111, 2.06694014,
         2.48161309, 4.21911985],
        [0.39611995, 0.64649606, 1.13215622, 1.51786046, 2.07033309,
         2.32762508, 3.86318429],
        [0.37993629, 0.62253291, 1.12174297, 1.51047609, 2.07534856,
         2.17269864, 3.5193786],
        [0.36311981, 0.59796794, 1.11141112, 1.50389813, 2.08219555,
         2.01815799, 3.18972386],
        [0.34577708, 0.57292671, 1.10122884, 1.49824561, 2.09109021,
         1.8652701, 2.87591642],
        [0.32802095, 0.54753544, 1.09126177, 1.49363716, 2.10225772,
         1.71522418, 2.57931895],
        [0.31097577, 0.52299945, 1.08097345, 1.48938039, 2.05910307,
         1.68755637, 2.4705595],
        [0.29553283, 0.50031601, 1.0697088, 1.48465828, 2.01373057,
         1.65113303, 2.35125468],
        [0.2814869, 0.47931181, 1.05734135, 1.4793911, 1.9661704,
         1.61624875, 2.24294162],
        [0.26866459, 0.45983004, 1.04372664, 1.47348009, 1.91649605,
         1.58280799, 2.14416819],
        [0.25691877, 0.44172934, 1.0287006, 1.46680151, 1.86483009,
         1.55072298, 2.05372724],
        [0.24612404, 0.42488265, 1.0120785, 1.45919837, 1.8113483,
         1.51991291, 1.97060708],
        [0.23617305, 0.40917598, 0.99365525, 1.45046877, 1.75628115,
         1.49030327, 1.8939534],
        [0.22697348, 0.3945071, 0.97320797, 1.44034904, 1.69991187,
         1.46182523, 1.82303985],
        [0.21844559, 0.38078435, 0.95050234, 1.42848901, 1.64257072,
         1.43441515, 1.75724494],
        [0.21052026, 0.36792557, 0.92530475, 1.414415, 1.58462523,
         1.40801405, 1.69603377],
        [0.20313726, 0.35585701, 0.89740247, 1.397473, 1.5264671,
         1.38256724, 1.63894345],
        [0.19624397, 0.34451244, 0.86663412, 1.37674133, 1.46849672,
         1.35802389, 1.58557141],
        [0.18979419, 0.33383231, 0.83293101, 1.35088923, 1.41110679,
         1.33433672, 1.53556584],
        [0.18374728, 0.323763, 0.79636643, 1.31795807, 1.35466677,
         1.31146171, 1.48861798],
        [0.17806727, 0.31425616, 0.75720385, 1.27502229, 1.29950956,
         1.28935779, 1.44445568],
        [0.17272232, 0.30526813, 0.71592857, 1.21773589, 1.24592155,
         1.26798661, 1.40283818],
        [0.16768408, 0.29675942, 0.67324352, 1.1400079, 1.19413659,
         1.24731233, 1.36355167],
        [0.16292728, 0.28869426, 0.63001667, 1.03495944, 1.14433385,
         1.22730141, 1.32640565],
        [0.1584293, 0.28104019, 0.58718372, 0.90005352, 1.09663915,
         1.20792244, 1.29122983],
        [0.15416985, 0.27376772, 0.54563088, 0.74681858, 1.05112886,
         1.18914593, 1.25787151]])

    age_wgts = np.ones(80) * 1 / 80
    abil_wgts = np.array([0.25, 0.25, 0.2, 0.1, 0.1, 0.09, 0.014])
    test_vals = income.get_e_orig(age_wgts, abil_wgts, plot=True)

    assert np.allclose(test_vals, expected_vals)


def test_get_e_orig_exception1():
    '''
    Test that RuntimeError is raised if age_wgts does not have length 80
    '''
    age_wgts = np.ones(70) * 1 / 80
    abil_wgts = np.array([0.25, 0.25, 0.2, 0.1, 0.1, 0.09, 0.014])
    with pytest.raises(RuntimeError):
        income.get_e_orig(age_wgts, abil_wgts)


def test_get_e_orig_exception2():
    '''
    Test that RuntimeError is raised if abil_wgts does not have length 87
    '''
    age_wgts = np.ones(80) * 1 / 80
    abil_wgts = np.array([0.25, 0.25, 0.2, 0.1, 0.1])
    with pytest.raises(RuntimeError):
        income.get_e_orig(age_wgts, abil_wgts)


def test_get_e_interp():
    '''
    Test of get_e_interp
    '''
    expected_vals = np.array([
       [0.42494207, 0.28466632, 0.3038266, 0.35719397, 0.44445965,
        0.72505425, 1.87898526],
       [0.4180863, 0.29955181, 0.33160091, 0.39468501, 0.49132198,
        0.77385826, 2.03879639],
       [0.41237957, 0.31497323, 0.36067077, 0.43426898, 0.54077514,
        0.82590159, 2.2093588],
       [0.40773253, 0.33092349, 0.39096563, 0.47584565, 0.59268652,
        0.88131842, 2.39094783],
       [0.40406625, 0.34739233, 0.42240171, 0.51929006, 0.64689283,
        0.94023572, 2.58377647],
       [0.40131077, 0.36436611, 0.45488256, 0.56445325, 0.70320139,
        1.00277084, 2.7879842],
       [0.39940367, 0.38182754, 0.48829978, 0.61116362, 0.76139208,
        1.06902877, 3.00362525],
       [0.398289, 0.39975553, 0.52253387, 0.65922856, 0.82121973,
        1.13909917, 3.23065656],
       [0.39791616, 0.41812496, 0.5574554, 0.70843665, 0.88241713,
        1.2130531, 3.46892559],
       [0.39823907, 0.43690651, 0.59292619, 0.75856008, 0.94469837,
        1.2909396, 3.71815816],
       [0.39921529, 0.45606648, 0.62880075, 0.80935745, 1.00776257,
        1.37278196, 3.97794668],
       [0.40080534, 0.47556672, 0.66492774, 0.86057684, 1.0712979,
        1.45857386, 4.24773894],
       [0.40297197, 0.49536444, 0.70115155, 0.91195898, 1.13498573,
        1.54827537, 4.52682784],
       [0.40567964, 0.51541221, 0.737314, 0.96324062, 1.19850488,
        1.64180888, 4.81434242],
       [0.40889388, 0.53565788, 0.77325593, 1.01415791, 1.26153591,
        1.73905494, 5.10924057],
       [0.41258082, 0.55604462, 0.80881894, 1.06444974, 1.32376526,
        1.83984827, 5.4103037],
       [0.4167067, 0.57651095, 0.84384702, 1.11386097, 1.38488923,
        1.94397384, 5.71613385],
       [0.42123744, 0.59699085, 0.8781881, 1.16214557, 1.44461771,
        2.0511632, 6.02515369],
       [0.42613821, 0.61741391, 0.91169563, 1.20906951, 1.50267762,
        2.16109126, 6.33560948],
       [0.43137307, 0.63770553, 0.94422995, 1.25441337, 1.55881592,
        2.27337344, 6.64557771],
       [0.4369046, 0.65778721, 0.97565958, 1.29797465, 1.61280226,
        2.38756354, 6.95297536],
       [0.44269359, 0.67757686, 1.0058624, 1.33956981, 1.66443114,
        2.50315227, 7.25557419],
       [0.44869879, 0.69698914, 1.03472664, 1.37903589, 1.71352367,
        2.61956677, 7.55101912],
       [0.45487661, 0.71593601, 1.06215171, 1.41623178, 1.75992879,
        2.73617103, 7.83685078],
       [0.46118094, 0.7343271, 1.08804891, 1.45103911, 1.80352405,
        2.8522676, 8.11053211],
       [0.467563, 0.75207041, 1.11234189, 1.48336282, 1.84421599,
        2.96710048, 8.36947892],
       [0.47397123, 0.7690728, 1.13496707, 1.51313132, 1.88194,
        3.0798594, 8.61109405],
       [0.48035118, 0.78524077, 1.15587372, 1.54029634, 1.91665988,
        3.18968558, 8.83280461],
       [0.4866456, 0.80048111, 1.17502405, 1.56483247, 1.94836702,
        3.29567897, 9.03210198],
       [0.49279443, 0.81470169, 1.19239304, 1.5867364, 1.97707921,
        3.39690705, 9.20658351],
       [0.49873498, 0.82781227, 1.20796818, 1.60602597, 2.00283925,
        3.49241512, 9.35399549],
       [0.50440215, 0.83972528, 1.22174906, 1.62273894, 2.02571334,
        3.58123799, 9.47227611],
       [0.5097287, 0.85035672, 1.23374687, 1.63693162, 2.04578929,
        3.6624131, 9.55959763],
       [0.51464564, 0.85962701, 1.24398379, 1.64867736, 2.06317456,
        3.73499473, 9.61440666],
       [0.51908272, 0.8674618, 1.25249229, 1.65806495, 2.07799432,
        3.79806918, 9.63546129],
       [0.52296896, 0.87379286, 1.25931435, 1.66519692, 2.09038936,
        3.85077069, 9.62186418],
       [0.52623328, 0.87855889, 1.2645007, 1.67018789, 2.10051417,
        3.89229768, 9.57309038],
       [0.52880528, 0.88170628, 1.2681099, 1.6731628, 2.10853486,
        3.92192909, 9.48900906],
       [0.53061597, 0.8831899, 1.27020756, 1.6742553, 2.11462734,
        3.93904027, 9.36989807],
       [0.53159871, 0.88297371, 1.27086535, 1.67360608, 2.11897548,
        3.94311818, 9.21645089],
       [0.53169013, 0.88103143, 1.27016023, 1.67136137, 2.12176947,
        3.93377533, 9.02977525],
       [0.53083109, 0.877347, 1.26817351, 1.66767148, 2.12320429,
        3.91076203, 8.81138317],
       [0.52896772, 0.87191508, 1.26499008, 1.66268943, 2.12347835,
        3.87397669, 8.56317247],
       [0.52605248, 0.8647413, 1.26069754, 1.65656978, 2.12279231,
        3.82347352, 8.28739982],
       [0.52204514, 0.85584251, 1.2553855, 1.64946753, 2.12134805,
        3.75946751, 7.98664584],
       [0.51691379, 0.84524688, 1.24914486, 1.64153715, 2.1193479,
        3.68233627, 7.66377305],
       [0.5106358, 0.83299383, 1.24206714, 1.63293176, 2.116994,
        3.59261858, 7.32187745],
       [0.50319867, 0.81913392, 1.23424386, 1.62380251, 2.11448784,
        3.49100949, 6.96423515],
       [0.49460078, 0.80372851, 1.22576608, 1.61429797, 2.11203006,
        3.37835197, 6.59424512],
       [0.48485201, 0.78684937, 1.21672381, 1.60456377, 2.10982036,
        3.25562519, 6.21536982],
       [0.47397418, 0.76857811, 1.20720571, 1.59474235, 2.10805769,
        3.12392963, 5.83107502],
       [0.46200137, 0.74900554, 1.19729864, 1.58497277, 2.10694053,
        2.98446932, 5.44477061],
       [0.44897994, 0.72823088, 1.18708744, 1.57539074, 2.10666742,
        2.83853152, 5.05975386],
       [0.4349684, 0.70636082, 1.17665465, 1.56612868, 2.1074377,
        2.68746456, 4.67915654],
       [0.42003702, 0.68350863, 1.16608035, 1.557316, 2.10945234,
        2.53265416, 4.30589743],
       [0.40426722, 0.659793, 1.15544206, 1.54907935, 2.11291508,
        2.37549897, 3.94264109],
       [0.3877507, 0.63533698, 1.14481464, 1.5415431, 2.1180337,
        2.21738605, 3.59176411],
       [0.37058835, 0.61026677, 1.13427029, 1.53482985, 2.12502152,
        2.05966685, 3.25532914],
       [0.35288892, 0.58471049, 1.12387858, 1.52906107, 2.13409911,
        1.90363441, 2.9350674],
       [0.33476758, 0.55879698, 1.11370651, 1.52435783, 2.14549631,
        1.75050239, 2.6323696],
       [0.31737182, 0.53375634, 1.10320659, 1.52001352, 2.10145407,
        1.72226552, 2.52137322],
       [0.30161126, 0.51060635, 1.09171025, 1.51519428, 2.05514837,
        1.68509303, 2.39961457],
       [0.28727644, 0.48917015, 1.07908843, 1.50981877, 2.00661,
        1.64949126, 2.28907376],
       [0.2741904, 0.46928768, 1.0651937, 1.50378618, 1.95591396,
        1.61536271, 2.18826879],
       [0.262203, 0.45081469, 1.04985861, 1.49697024, 1.90318535,
        1.58261778, 2.09596768],
       [0.25118625, 0.43362151, 1.03289463, 1.48921072, 1.84860357,
        1.55117402, 2.01113793],
       [0.24103059, 0.41759179, 1.01409245, 1.48030158, 1.79240381,
        1.52095537, 1.93290766],
       [0.2316418, 0.4026212, 0.99322461, 1.4699737, 1.73487514,
        1.49189161, 1.86053558],
       [0.22293851, 0.38861621, 0.97005199, 1.45786973, 1.67635462,
        1.46391776, 1.79338742],
       [0.21485017, 0.37549295, 0.94433614, 1.44350626, 1.61721732,
        1.43697366, 1.73091727],
       [0.20731532, 0.36317617, 0.91585997, 1.426216, 1.55786302,
        1.41100346, 1.67265274],
       [0.20028025, 0.35159827, 0.88445879, 1.40505773, 1.49870031,
        1.38595531, 1.61818296],
       [0.19369782, 0.34069848, 0.85006249, 1.37867391, 1.44013,
        1.36178096, 1.5671489],
       [0.18752653, 0.33042206, 0.81274585, 1.34506543, 1.38252914,
        1.33843546, 1.51923542],
       [0.18172971, 0.32071969, 0.77277779, 1.30124656, 1.32623748,
        1.31587691, 1.47416481],
       [0.17627482, 0.31154679, 0.73065357, 1.24278191, 1.27154729,
        1.29406617, 1.43169133],
       [0.17113296, 0.30286308, 0.68709059, 1.16345524, 1.21869723,
        1.27296667, 1.39159679],
       [0.16627832, 0.29463204, 0.64297466, 1.05624617, 1.16787017,
        1.25254418, 1.35368676],
       [0.16168782, 0.28682054, 0.59926074, 0.91856555, 1.11919449,
        1.23276662, 1.31778745],
       [0.15734076, 0.27939849, 0.55685325, 0.76217892, 1.07274816,
        1.21360393, 1.28374303]])

    age_wgts = np.ones(80) * 1 / 80
    abil_wgts = np.array([0.25, 0.25, 0.2, 0.1, 0.1, 0.09, 0.01])
    test_vals = income.get_e_interp(
        80, age_wgts, age_wgts, abil_wgts)

    assert np.allclose(test_vals, expected_vals)
