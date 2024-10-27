from Crypto.Util.number import*
from secret import flag


m = bytes_to_long(flag)
p = getPrime(1024)
q = getPrime(1024)
n = p*q
e = 65537
c = pow(m,e,n)
pq = (p-1)*(q-2)
qp = (q-1)*(p-2)
p_q = p + q


print(f"{c = }")
print(f"{pq = }")
print(f"{qp = }")
print(f"{n = }")
print(f"{p_q = }")
'''
c = 5654386228732582062836480859915557858019553457231956237167652323191768422394980061906028416785155458721240012614551996577092521454960121688179565370052222983096211611352630963027300416387011219744891121506834201808533675072141450111382372702075488292867077512403293072053681315714857246273046785264966933854754543533442866929316042885151966997466549713023923528666038905359773392516627983694351534177829247262148749867874156066768643169675380054673701641774814655290118723774060082161615682005335103074445205806731112430609256580951996554318845128022415956933291151825345962528562570998777860222407032989708801549746
pq = 18047017539289114275195019384090026530425758236625347121394903879980914618669633902668100353788910470141976640337675700570573127020693081175961988571621759711122062452192526924744760561788625702044632350319245961013430665853071569777307047934247268954386678746085438134169871118814865536503043639618655569687154230787854196153067547938936776488741864214499155892870610823979739278296501074632962069426593691194105670021035337609896886690049677222778251559566664735419100459953672218523709852732976706321086266274840999100037702428847290063111455101343033924136386513077951516363739936487970952511422443500922412450462
qp = 18047017539289114275195019384090026530425758236625347121394903879980914618669633902668100353788910470141976640337675700570573127020693081175961988571621759711122062452192526924744760561788625702044632350319245961013430665853071569777307047934247268954386678746085438134169871118814865536503043639618655569687077087914198877794354459669808240133383828356379423767736753506794441545506312066344576298453957064590180141648690226266236642320508613544047037110363523129966437840660693885863331837516125853621802358973786440314619135781324447765480391038912783714312479080029167695447650048419230865326299964671353746764860
n = 18047017539289114275195019384090026530425758236625347121394903879980914618669633902668100353788910470141976640337675700570573127020693081175961988571621759711122062452192526924744760561788625702044632350319245961013430665853071569777307047934247268954386678746085438134169871118814865536503043639618655569687534959910892789661065614807265825078942931717855566686073463382398417205648946713373617006449901977718981043020664616841303517708207413215548110294271101267236070252015782044263961319221848136717220979435486850254298686692230935985442120369913666939804135884857831857184001072678312992442792825575636200505903
p_q = 279533706577501791569740668595544511920056954944184570513187478007551195831693428589898548339751066551225424790534556602157835468618845221423643972870671556362200734472399328046960316064864571163851111207448753697980178391430044714097464866523838747053135392202848167518870720149808055682621080992998747265496
'''