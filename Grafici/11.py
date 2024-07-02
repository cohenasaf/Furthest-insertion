import matplotlib.pyplot as plt
import numpy as np

l = [('eil51', 1), ('berlin52', 1), ('st70', 2), ('pr76', 1), ('eil76', 1), ('rat99', 1), ('kroD100', 3), ('kroA100', 1), ('kroC100', 1), ('kroB100', 1), ('kroE100', 1), ('rd100', 1), ('eil101', 1), ('lin105', 1), ('pr107', 3), ('pr124', 3), ('bier127', 2), ('ch130', 3), ('pr136', 1), ('pr144', 3), ('kroA150', 3), ('ch150', 1), ('kroB150', 3), ('pr152', 1), ('u159', 3), ('rat195', 1), ('d198', 3), ('kroA200', 1), ('kroB200', 3), ('ts225', 2), ('tsp225', 3), ('pr226', 1), ('gil262', 1), ('pr264', 3), ('a280', 1), ('pr299', 2), ('lin318', 3), ('linhp318', 3), ('rd400', 3), ('fl417', 1), ('pr439', 2), ('pcb442', 3), ('d493', 1), ('u574', 3), ('rat575', 3), ('p654', 3), ('d657', 3), ('u724', 3), ('rat783', 3), ('pr1002', 2)]
dF = {'eil51': 3, 'berlin52': 3, 'st70': 3, 'pr76': 3, 'eil76': 5, 'rat99': 3, 'kroD100': 3, 'kroA100': 3, 'kroC100': 3, 'kroB100': 3, 'kroE100': 3, 'rd100': 3, 'eil101': 5, 'lin105': 3, 'pr107': 3, 'pr124': 3, 'bier127': 6, 'ch130': 3, 'pr136': 3, 'pr144': 3, 'kroA150': 5, 'ch150': 4, 'kroB150': 3, 'pr152': 3, 'u159': 3, 'rat195': 5, 'd198': 6, 'kroA200': 5, 'kroB200': 3, 'ts225': 6, 'tsp225': 4, 'pr226': 3, 'gil262': 6, 'pr264': 6, 'a280': 6, 'pr299': 3, 'lin318': 5, 'linhp318': 5, 'rd400': 6, 'fl417': 3, 'pr439': 6, 'pcb442': 6, 'd493': 6, 'u574': 6, 'rat575': 5, 'p654': 3, 'd657': 6, 'u724': 6, 'rat783': 6, 'pr1002': 6}

# Sample data (4 lists)
x = [x[0] for x in l[:50]]

#y1 = [np.float64(8.65340232849121e-05), np.float64(9.701251983642578e-05), np.float64(0.00016402006149291993), np.float64(0.00019356012344360352), np.float64(0.0001797199249267578), np.float64(0.00032025575637817383), np.float64(0.00029244422912597654), np.float64(0.00030351877212524413), np.float64(0.000303184986114502), np.float64(0.00029354095458984376), np.float64(0.0003076910972595215), np.float64(0.0002876400947570801), np.float64(0.00030068159103393557), np.float64(0.0003563284873962402), np.float64(0.00033112764358520506), np.float64(0.00045261383056640627), np.float64(0.00045734643936157227), np.float64(0.0005153775215148926), np.float64(0.0005715131759643554), np.float64(0.0006989240646362305), np.float64(0.000762486457824707), np.float64(0.0006881356239318848), np.float64(0.0008616805076599121), np.float64(0.0006976604461669921), np.float64(0.0007466673851013184), np.float64(0.0011410474777221679), np.float64(0.0011929035186767577), np.float64(0.0011620521545410156), np.float64(0.0011531472206115722), np.float64(0.0014202237129211427), np.float64(0.0014212846755981446), np.float64(0.0015857219696044922), np.float64(0.0021352887153625487), np.float64(0.0022001266479492188), np.float64(0.0022487640380859375), np.float64(0.0027320504188537596), np.float64(0.002919721603393555), np.float64(0.00323638916015625), np.float64(0.004962444305419922), np.float64(0.00550844669342041), np.float64(0.006130361557006836), np.float64(0.006524777412414551), np.float64(0.007819557189941406), np.float64(0.011308133602142334), np.float64(0.011736905574798584), np.float64(0.014712607860565186), np.float64(0.01567678451538086), np.float64(0.019019699096679686), np.float64(0.023387932777404787), np.float64(0.03549848794937134)]
#y2 = [np.float64(0.001078629493713379), np.float64(0.001213407516479492), np.float64(0.0019734740257263184), np.float64(0.0023717284202575684), np.float64(0.0023241281509399415), np.float64(0.003975319862365723), np.float64(0.004042291641235351), np.float64(0.00403064489364624), np.float64(0.004037296772003174), np.float64(0.004046404361724853), np.float64(0.0040278792381286625), np.float64(0.004004812240600586), np.float64(0.0041029095649719235), np.float64(0.004407894611358642), np.float64(0.004566752910614013), np.float64(0.006202471256256103), np.float64(0.00641857385635376), np.float64(0.006761205196380615), np.float64(0.007393848896026611), np.float64(0.008766376972198486), np.float64(0.009590888023376464), np.float64(0.0090012788772583), np.float64(0.009851658344268798), np.float64(0.00939549207687378), np.float64(0.010086190700531007), np.float64(0.0152573823928833), np.float64(0.01569697856903076), np.float64(0.01583552360534668), np.float64(0.016022038459777833), np.float64(0.020305824279785157), np.float64(0.0202730655670166), np.float64(0.020534753799438477), np.float64(0.027779507637023925), np.float64(0.027945387363433837), np.float64(0.031120169162750243), np.float64(0.03549004793167114), np.float64(0.04034898281097412), np.float64(0.04153977632522583), np.float64(0.06562156677246093), np.float64(0.0717149019241333), np.float64(0.07825087308883667), np.float64(0.08012900352478028), np.float64(0.09939961433410645), np.float64(0.13772478103637695), np.float64(0.13795710802078248), np.float64(0.18144257068634034), np.float64(0.1834063410758972), np.float64(0.22600994110107422), np.float64(0.2666385531425476), np.float64(0.44593489170074463)]
#y3 = [np.float64(0.002815353870391846), np.float64(0.003134119510650635), np.float64(0.006162726879119873), np.float64(0.006783699989318848), np.float64(0.00718010663986206), np.float64(0.011507892608642578), np.float64(0.013425695896148681), np.float64(0.012011349201202393), np.float64(0.012015593051910401), np.float64(0.012113285064697266), np.float64(0.011899280548095702), np.float64(0.01200706958770752), np.float64(0.012407982349395752), np.float64(0.013215470314025878), np.float64(0.01521146297454834), np.float64(0.01936671733856201), np.float64(0.021274268627166748), np.float64(0.021877813339233398), np.float64(0.022971224784851075), np.float64(0.028788816928863526), np.float64(0.03111586570739746), np.float64(0.027599453926086426), np.float64(0.03291893005371094), np.float64(0.028952622413635255), np.float64(0.03426494598388672), np.float64(0.04954049587249756), np.float64(0.05284991264343262), np.float64(0.05088553428649902), np.float64(0.05575640201568603), np.float64(0.07101272344589234), np.float64(0.07176033258438111), np.float64(0.06623106002807617), np.float64(0.09340779781341553), np.float64(0.10029189586639405), np.float64(0.10462532043457032), np.float64(0.12590534687042237), np.float64(0.14342401027679444), np.float64(0.14833419322967528), np.float64(0.24896911382675171), np.float64(0.25115551948547366), np.float64(0.304039454460144), np.float64(0.30888866186141967), np.float64(0.3581228494644165), np.float64(0.5597206354141235), np.float64(0.5631559729576111), np.float64(0.7357736706733704), np.float64(0.7256323218345642), np.float64(0.9040811896324158), np.float64(1.1239006519317627), np.float64(1.8122980833053588)]
#y4 = [np.float64(0.001146519184112549), np.float64(0.0012389898300170898), np.float64(0.002122080326080322), np.float64(0.002535557746887207), np.float64(0.002467620372772217), np.float64(0.004214560985565186), np.float64(0.004293370246887207), np.float64(0.0042752385139465336), np.float64(0.004283761978149414), np.float64(0.004332053661346436), np.float64(0.004279887676239014), np.float64(0.004245984554290772), np.float64(0.004376709461212158), np.float64(0.00470430850982666), np.float64(0.004827713966369629), np.float64(0.006607508659362793), np.float64(0.0068383455276489254), np.float64(0.007198548316955567), np.float64(0.007862865924835205), np.float64(0.009176456928253173), np.float64(0.009913766384124756), np.float64(0.009618473052978516), np.float64(0.010942196846008301), np.float64(0.009910130500793457), np.float64(0.010824751853942872), np.float64(0.017008697986602782), np.float64(0.01682215929031372), np.float64(0.01704235076904297), np.float64(0.01706486940383911), np.float64(0.021667826175689697), np.float64(0.021806466579437255), np.float64(0.02189122438430786), np.float64(0.030229854583740234), np.float64(0.029902398586273193), np.float64(0.033935940265655516), np.float64(0.038852500915527347), np.float64(0.04386240243911743), np.float64(0.04503244161605835), np.float64(0.07160940170288085), np.float64(0.0779498815536499), np.float64(0.0858218789100647), np.float64(0.08805950880050659), np.float64(0.11032209396362305), np.float64(0.1504093289375305), np.float64(0.15100610256195068), np.float64(0.198323392868042), np.float64(0.19978007078170776), np.float64(0.24637939929962158), np.float64(0.2897894620895386), np.float64(0.47960623502731325)]
#y5 = [np.float64(0.0035837173461914064), np.float64(0.0043140769004821776), np.float64(0.006754922866821289), np.float64(0.008419334888458252), np.float64(0.008178257942199707), np.float64(0.014429199695587158), np.float64(0.014025998115539551), np.float64(0.014470994472503662), np.float64(0.014418137073516846), np.float64(0.014566993713378907), np.float64(0.014083611965179443), np.float64(0.014409899711608887), np.float64(0.015262901782989502), np.float64(0.01664937734603882), np.float64(0.01896378993988037), np.float64(0.03363956212997436), np.float64(0.024972128868103027), np.float64(0.024062716960906984), np.float64(0.02702723741531372), np.float64(0.036403107643127444), np.float64(0.03416283130645752), np.float64(0.03192633390426636), np.float64(0.034521055221557614), np.float64(0.03821207284927368), np.float64(0.038854897022247314), np.float64(0.056626510620117185), np.float64(0.05953048467636109), np.float64(0.0570411205291748), np.float64(0.058214211463928224), np.float64(0.07657123804092407), np.float64(0.07523136138916016), np.float64(0.17432600259780884), np.float64(0.10156099796295166), np.float64(0.10446007251739502), np.float64(0.11605685949325562), np.float64(0.13510955572128297), np.float64(0.14963217973709106), np.float64(0.15349539518356323), np.float64(0.2390868306159973), np.float64(0.4764948010444641), np.float64(0.30259616374969484), np.float64(0.30592180490493776), np.float64(0.40245517492294314), np.float64(0.5025433421134948), np.float64(0.5064205527305603), np.float64(1.1844215393066406), np.float64(0.674577271938324), np.float64(0.8486524105072022), np.float64(0.9552456974983216), np.float64(1.6152544856071471)]
y1 = [np.float64(8.454322814941407e-05), np.float64(8.958578109741211e-05), np.float64(0.0001629471778869629), np.float64(0.0001922130584716797), np.float64(0.00018447637557983398), np.float64(0.0003374934196472168), np.float64(0.00030951499938964845), np.float64(0.00031464099884033204), np.float64(0.0003411412239074707), np.float64(0.0003174781799316406), np.float64(0.0003140568733215332), np.float64(0.0003026723861694336), np.float64(0.000301969051361084), np.float64(0.00034883022308349607), np.float64(0.0003482222557067871), np.float64(0.0004646539688110352), np.float64(0.000477445125579834), np.float64(0.0005017280578613281), np.float64(0.0005733609199523926), np.float64(0.000648665428161621), np.float64(0.000666666030883789), np.float64(0.0007115840911865234), np.float64(0.0007051944732666016), np.float64(0.0007130026817321778), np.float64(0.000742959976196289), np.float64(0.001154649257659912), np.float64(0.0012195587158203125), np.float64(0.001172637939453125), np.float64(0.0011831998825073242), np.float64(0.0015148162841796876), np.float64(0.0014624357223510741), np.float64(0.0016399502754211425), np.float64(0.002089560031890869), np.float64(0.002383124828338623), np.float64(0.002454853057861328), np.float64(0.0030557036399841307), np.float64(0.0031891584396362303), np.float64(0.0032860398292541503), np.float64(0.005372369289398193), np.float64(0.00597296953201294), np.float64(0.006746077537536621), np.float64(0.006966781616210937), np.float64(0.00807781219482422), np.float64(0.011986935138702392), np.float64(0.01193329095840454), np.float64(0.014690375328063965), np.float64(0.015572631359100341), np.float64(0.0190476655960083), np.float64(0.022987401485443114), np.float64(0.03528292179107666)]
y2 = [np.float64(0.0010567545890808106), np.float64(0.0011263370513916015), np.float64(0.002013075351715088), np.float64(0.0023537397384643553), np.float64(0.0023308396339416504), np.float64(0.004131293296813965), np.float64(0.004084920883178711), np.float64(0.004071259498596191), np.float64(0.0044286131858825685), np.float64(0.0041007399559021), np.float64(0.004142630100250244), np.float64(0.004024326801300049), np.float64(0.004079043865203857), np.float64(0.00452655553817749), np.float64(0.004670274257659912), np.float64(0.006261885166168213), np.float64(0.006482398509979248), np.float64(0.006792449951171875), np.float64(0.007437789440155029), np.float64(0.008371520042419433), np.float64(0.009393894672393798), np.float64(0.009363400936126708), np.float64(0.009339678287506103), np.float64(0.009387397766113281), np.float64(0.010055959224700928), np.float64(0.015041875839233398), np.float64(0.01569863557815552), np.float64(0.01597268581390381), np.float64(0.016147875785827638), np.float64(0.02037688493728638), np.float64(0.020249390602111818), np.float64(0.02062646150588989), np.float64(0.027897965908050538), np.float64(0.02943465709686279), np.float64(0.0317987322807312), np.float64(0.036245858669281004), np.float64(0.040598273277282715), np.float64(0.04120248556137085), np.float64(0.06631778478622437), np.float64(0.0723342776298523), np.float64(0.07955466508865357), np.float64(0.08098876476287842), np.float64(0.10073293447494507), np.float64(0.13651642799377442), np.float64(0.13777718544006348), np.float64(0.18273501396179198), np.float64(0.18195998668670654), np.float64(0.22435429096221923), np.float64(0.26446679830551145), np.float64(0.44777736663818357)]
y3 = [np.float64(0.0027266860008239744), np.float64(0.002874314785003662), np.float64(0.006314754486083984), np.float64(0.00672757625579834), np.float64(0.007203066349029541), np.float64(0.01187288761138916), np.float64(0.013963699340820312), np.float64(0.012636721134185791), np.float64(0.013923704624176025), np.float64(0.012293517589569092), np.float64(0.012510275840759278), np.float64(0.012063121795654297), np.float64(0.01221921443939209), np.float64(0.013117361068725585), np.float64(0.015741407871246338), np.float64(0.01929340362548828), np.float64(0.021439719200134277), np.float64(0.021698033809661864), np.float64(0.023355257511138917), np.float64(0.027884197235107423), np.float64(0.028961360454559326), np.float64(0.027661716938018797), np.float64(0.028914833068847658), np.float64(0.029104697704315185), np.float64(0.034023392200469973), np.float64(0.04846422672271729), np.float64(0.052368903160095216), np.float64(0.05064992904663086), np.float64(0.05589789152145386), np.float64(0.07129135131835937), np.float64(0.07147525548934937), np.float64(0.06613667011260986), np.float64(0.09166746139526367), np.float64(0.10482182502746581), np.float64(0.10562653541564941), np.float64(0.1281762719154358), np.float64(0.1467496156692505), np.float64(0.14492560625076295), np.float64(0.2532459139823914), np.float64(0.25090601444244387), np.float64(0.30799552202224734), np.float64(0.3117732644081116), np.float64(0.3594714283943176), np.float64(0.5591420531272888), np.float64(0.5653339624404907), np.float64(0.7346496105194091), np.float64(0.7303634762763977), np.float64(0.907025420665741), np.float64(1.1330915093421936), np.float64(1.8185113430023194)]
y4 = [np.float64(0.0010565996170043945), np.float64(0.001104259490966797), np.float64(0.001978790760040283), np.float64(0.0023339509963989256), np.float64(0.002298140525817871), np.float64(0.003995823860168457), np.float64(0.004131424427032471), np.float64(0.004120934009552002), np.float64(0.004421877861022949), np.float64(0.004067254066467285), np.float64(0.0042236089706420895), np.float64(0.0039926648139953615), np.float64(0.004168236255645752), np.float64(0.004389667510986328), np.float64(0.004582536220550537), np.float64(0.006088829040527344), np.float64(0.0064203858375549315), np.float64(0.006667006015777588), np.float64(0.007414770126342773), np.float64(0.008228158950805664), np.float64(0.008874630928039551), np.float64(0.008977663516998292), np.float64(0.008895456790924072), np.float64(0.009211456775665284), np.float64(0.009992384910583496), np.float64(0.015126979351043702), np.float64(0.015676391124725342), np.float64(0.015811407566070558), np.float64(0.015932726860046386), np.float64(0.02024301290512085), np.float64(0.02023392915725708), np.float64(0.02080674171447754), np.float64(0.027636182308197022), np.float64(0.0287591814994812), np.float64(0.032321703433990476), np.float64(0.03633426427841187), np.float64(0.04174284934997559), np.float64(0.04119710922241211), np.float64(0.06801977157592773), np.float64(0.07366375923156739), np.float64(0.08141399621963501), np.float64(0.08362482786178589), np.float64(0.10088763236999512), np.float64(0.13925547599792482), np.float64(0.13983161449432374), np.float64(0.1836087465286255), np.float64(0.18520991802215575), np.float64(0.22758538722991944), np.float64(0.26685911417007446), np.float64(0.44950356483459475)]
y5 = [np.float64(0.0034957051277160643), np.float64(0.0039733052253723145), np.float64(0.006773912906646728), np.float64(0.007962405681610107), np.float64(0.008172523975372315), np.float64(0.014447450637817383), np.float64(0.014132153987884522), np.float64(0.014369595050811767), np.float64(0.01564580202102661), np.float64(0.014264357089996339), np.float64(0.014042198657989502), np.float64(0.014011549949645995), np.float64(0.015086042881011962), np.float64(0.015979862213134764), np.float64(0.01914999485015869), np.float64(0.03115837574005127), np.float64(0.025075638294219972), np.float64(0.02355184555053711), np.float64(0.026552772521972655), np.float64(0.034457623958587646), np.float64(0.031040680408477784), np.float64(0.03158704042434692), np.float64(0.031938588619232176), np.float64(0.03778378963470459), np.float64(0.03720014095306397), np.float64(0.05359106063842774), np.float64(0.05887467861175537), np.float64(0.056303775310516356), np.float64(0.05724776983261108), np.float64(0.07552659511566162), np.float64(0.07444695234298707), np.float64(0.16043840646743773), np.float64(0.0982922911643982), np.float64(0.10684403181076049), np.float64(0.11837248802185059), np.float64(0.13547412157058716), np.float64(0.1504114270210266), np.float64(0.1512665033340454), np.float64(0.24175543785095216), np.float64(0.5303916931152344), np.float64(0.30409678220748904), np.float64(0.3041113495826721), np.float64(0.40255863666534425), np.float64(0.5006414175033569), np.float64(0.4986427903175354), np.float64(1.1007047653198243), np.float64(0.6688896298408509), np.float64(0.837908136844635), np.float64(0.9440253853797913), np.float64(1.5900795459747314)]


plt.figure(figsize=(14, 6))

plt.plot(x, y1, marker='o', color='blue', label='Nearest Neighbor')
plt.plot(x, y2, marker='s', color='red', label='Nearest Insertion')
plt.plot(x, y3, marker='d', color='purple', label='Cheapest Insertion versione 3')
plt.plot(x, y4, marker='^', color='green', label='Farthest Insertion')
plt.plot(x, y5, marker='*', color='orange', label='Furthest Insertion versione 2')

plt.xticks(rotation=45)
plt.xlabel('Prime 30 istanze TSP da TSP-LIB')
plt.ylabel('Tempi medi (secondi)')
plt.yscale('log')
plt.title('Tempi medi per le prime 50 istanze dal TSP-LIB')
plt.legend()  # Show legend based on labels

plt.grid(True)
plt.tight_layout()
plt.savefig("/home/asaf/Desktop/Furthest-insertion/Grafici/11.png")
plt.show()

