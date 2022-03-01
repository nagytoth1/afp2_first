# Követelmény specifikáció

### Áttekintés



### Jelenlegi helyzet



### Vágyálomrendszer

	- Tudjuk nyomon követni a rendszeridõt (naplózás és a hallgatók idõbeli igazodása szempontjából fontos)
	- 45 percenként figyelmeztessen (hallgató álljon fel a géptõl, mozogjon)
	- Jó lenne, ha adatbázis-kapcsolatot használhatnánk a késõbbiekben a feladatra adott válaszok pontszámainak tárolására (a session idejére).
	- Jó lenne, ha meg tudnánk nézni a weboldal látogatásainak idõpontjait naplózás szempontjából.
	- Szeretnénk, hogy az weboldal gördülékenyen reagáljon, legyen reszponzív.
	- Az adatbázis legyen egy internetes repozitóriumból elérhetõ

### Elvárások


## Követelménylista

|    Modul    	| ID |       Név        	|                                                        Kifejtés                                                       		|
|-------------	|----|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Interface   	| I1 | Menüsor   		| Ne legyen túlgondolva, a PTI-s tárgyak legyenek kilistázva, ezekre kattintva átvisz a megfelelõ oldal feladatlistájára. 		|
| Interface	| I2 | Felhasználói felület	| A teljes felhasználói felület legyen leegyszerûsített, minimalista.									|
| Interface 	| I3 | Egyéb hivatkozások      	| Legyenek hivatkozások a suli honlapjára, Neptun-oldalára, az e-learning-oldalra							|
| Interface	| I4 | Feladatkiosztó		| A feladatok sablonjait töltsük ki az adatbázisból olvasott adatokkal.									|
| Datastore 	| D1 | Adattárolási mód 	| Egy adatbázis-táblában eltároljuk a különbözõ tárgyakhoz kapcsolódó feladatok részleteit, ezek megfelelõ helyekre beollózva.		|
| Datastore 	| D2 | Tervezett karbantartás	| A feladatok adatbázisa félévek kezdete elõtti héten legyen takarítva, lehetõleg inkább egyre bõvebb készlet álljon rendelkezésre.	|
| Datastore 	| D3 | Adatbázis        	| Tároljuk az adatokat adatbázisban, szerkezete legyen a lehetõ legegyszerûbb, mivel sok feladat részleteit fogunk tárolni. 		|
| Feature   	| F1 | Rendszeridõ      	| Mutasson rendszeridõt a képernyõ valamely, a munka szempontjából kevésbé zavaró részén.						|
| Feature   	| F2 | Random adatolvasás      	| Az adatbázisból olvassunk ki véletlenszerûen egy rekordot (egy feladat-csomagot) a tárgynak megfelelõ rekeszekbõl.			|

### Rendszerre vonatkozó törvények

**Kivonat: 18/2018. (V. 31.) utasítás az Informatikai Biztonsági Szabályzatról**
	<p>	*171.* 	Az operációs rendszer, az alkalmazás és a hálózati aktív eszköz szoftver verzióját, valamint biztonsági patch szintjét tesztelést követõen lehetõség szerint a gyártói támogatással rendelkezõ, legmagasabb szintre kell hozni.(…) </p>
	<p>	*177.* 	Meglévõ rendszer esetén a biztonságot közvetlenül veszélyeztetõ hibákat a lehetõ leghamarabb javítani kell, vagy korrektív kontroll alkalmazásával csökkenteni a kockázatokat. Új rendszer esetén feltárt sérülékenységet a használatbavételig javítani kell. </p>
	<p>	*178.* 	A hálózatok ki- és bemeneteli pontjait minimalizálni kell, továbbá a ki- és bemeneti pontok adatforgalmát elektronikusan naplózni, és a naplófájlokat ellenõrizni kell.</p>
	<p>	*179.* 	Az informatikai üzemeltetésért felelõs vezetõnek a rendszer minden arra alkalmas – megfelelõ hardver- és szoftverkörnyezettel rendelkezõ – elemére jóváhagyott, központilag rendszeresített vírusellenõrzõ szoftvert kell telepítenie és naprakészen tartania.(…)</p>
	<p>	*183.* 	A biztonsági mentés célja az információ és az adatfeldolgozó szoftverek épségének és rendelkezésre állásának biztosítása. A hatékony biztonsági adatmentés érdekében a munkaállomásokon feldolgozott adatállományokat tárolni kizárólag szervereken és központi kiszolgálókon, valamint az adatmentésre szolgáló médián lehet. Bármilyen más helyen történõ adattárolás még átmenetileg is tilos.(…)</p>
	<p>	*200.* 	Tilos a hálózat biztonságos mûködését zavaró vagy veszélyeztetõ információk, programok terjesztése. (…)</p>
	<p>	*208.* 	A rendszert és a hálózatot túlterheléses – szolgáltatás megtagadás jellegû – támadásokkal szembeni védelemmel kell ellátni.(…)</p>
	<p>	*222.* 	A fejlesztés során a biztonságos programozás irányelveit kell követni. A szoftverfejlesztés során a szoftver funkcionalitása mellett fokozott figyelmet kell fordítani a rendszer és a kapcsolódó rendszerek biztonsági követelményeinek betartására is.</p>
	<p>	*forrás: NJT* </p>

#### Szerzõi jogok
**Kivonat az 1999. évi LXXVI. szerzõi jogi törvénybõl:**
	<p>*1.§* 	(2) Szerzõi jogi védelem alá tartozik – függetlenül attól, hogy e törvény megnevezi-e – 
				az irodalom, a tudomány és a mûvészet minden alkotása. Ilyen alkotásnak minõsül különösen: (...)</p>
			<p>&emsp; &emsp;c) a *számítógépi programalkotás és a hozzá tartozó dokumentáció (a továbbiakban: szoftver) akár forráskódban, akár tárgykódban vagy bármilyen más formában* rögzített minden fajtája, ideértve a felhasználói programot és az operációs rendszert is.(...)</p>
			<p>&emsp;(3) A szerzõi jogi védelem az alkotást a szerzõ szellemi tevékenységébõl fakadó egyéni, eredeti jellege alapján illeti meg. A védelem nem függ mennyiségi, minõségi, esztétikai jellemzõktõl vagy az alkotás színvonalára vonatkozó értékítélettõl. (...)</p>
	<p>*4.$* (1) A szerzõi jog *azt illeti, aki a mûvet megalkotta* (szerzõ). </p>
			<p>&emsp;(2) *Szerzõi jogi védelem* alatt áll – az eredeti mû szerzõjét megilletõ jogok sérelme nélkül – más szerzõ mûvének átdolgozása, feldolgozása vagy fordítása is, ha annak egyéni, eredeti jellege van.(...)</p>
	<p>*5.§* (1) Több szerzõ közös mûvére, ha annak részei nem használhatók fel önállóan, a szerzõi jog együttesen és – kétség esetén – egyenlõ arányban illeti meg a szerzõtársakat; a szerzõi jog megsértése ellen azonban bármelyik szerzõtárs önállóan is felléphet. (...)</p>
	<p>*13.§* A szerzõ személyhez fûzõdõ jogát sérti mûvének a becsületére vagy jóhírnevére sérelmes mindenfajta eltorzítása, megcsonkítása, megváltoztatása és a mûvel kapcsolatos más ilyen jellegû visszaélés.(...)</p>
	<p>*42.§* (1) Felhasználási szerzõdés alapján a szerzõ engedélyt ad mûvének a felhasználására, a felhasználó pedig köteles ennek fejében díjat fizetni. (...)</p>
	<p>*59.§* (1) Eltérõ megállapodás hiányában a szerzõ kizárólagos joga nem terjed ki a többszörözésre, az átdolgozásra, a feldolgozásra, a fordításra, a szoftver bármely más módosítására – ideértve a hiba kijavítását is –, valamint ezek eredményének többszörözésére annyiban, amennyiben e felhasználási cselekményeket a szoftvert jogszerûen megszerzõ személy a szoftver rendeltetésével összhangban végzi.</p>
			<p>&emsp;(2) A felhasználási szerzõdésben sem zárható ki, hogy a felhasználó egy biztonsági másolatot készíthessen a szoftverrõl, ha az a felhasználáshoz szükséges.</p>
			<p>&emsp;(3) Aki a szoftver valamely példányának felhasználására jogosult, a szerzõ engedélye nélkül is megfigyelheti és tanulmányozhatja a szoftver mûködését, továbbá kipróbálhatja a szoftvert annak betáplálása, képernyõn való megjelenítése, futtatása, továbbítása vagy tárolása során abból a célból, hogy a szoftver valamely elemének alapjául szolgáló elgondolást vagy elvet megismerje.</p>
<p>(Forrás: NJT)</p>

### Általános Információk

Az Alkalmazásnak a használatát és a hozzáférését megelõzi az alkalmazandó jogszabályok és a jelen Felhasználási Feltételek
és Adatkezelési tájékoztatóknak az elolvasása és értelmezése. Amennyiben az alkalmazást letöltõk vagy használók (a késõbbiekben: a Felhasználók)
elfogadják és teljesítik az imént említett Felhasználási Feltételeket abban az esetben az alkalmazás használata engedélyezett. Amennyiben ezen
Adatkezelési Tájékoztatót és a Felhasználói Feltételek nem fogadják el, abban az esetben a Felhasználó nem jogosult arra hogy az alkalmazást használhassa.

A jelenlegi Felhasználási Feltételekre a magyar jog az irányadó, tekintet nélkül a nemzetközi magánjog elõírásaira. Az Alkalmazás Felhasználói
kifejezetten hozzájárulnak ahhoz, hogy a jogvitákra a magyar hatóságoknak és bíróságoknak legyen kizárólags joghatóságuk a magyar jog alapján.

### Szellemi tulajdon

Az Alkalmazás és valamennyi kapcsolódó védjegy, szerzõi jogi alkotás és egyéb - akár bejegyzett, akár be nem jegyzett - szellemi tulajdon
(a továbbiakban együttesen: Szellemi Tulajdon) tulajdonosa az EKE és/vagy EKE Szolgáltató, valamint az alkalmazáshoz kedvezményt nyújtó
partnerek. A Felhasználók az Alkalmazást a Szellemi Tulajdon maximális tiszteletben tartásával jogosultak használni. 

A Szellemi Tulajdon kiterjed különösen, de nem kizárólagosan valamennyi szoftverre, logóra, márkajelre, márkanévre, fényképre, szövegre, grafikára, adatbázisra.
A Szellemi Tulajdonnak tilos bárminemû megsértése, bitorlása, másolása, átdolgozása és tilos azt bármilyen egyéb módon megsérteni,
azt jogosulatlanul felhasználni, továbbadni, megterhelni, azzal bármilyen módon rendelkezni, visszaélni. 

Ezen szabályok megsértése az Alkalmazás használati lehetõségeinek azonnali hatályú megszüntetése mellett a megfelelõ jogi lépések megtételét
– beleértve esetleges büntetõjogi lépések megtételét is – vonja maga után a Felhasználóval, más jogsértõ személlyel szemben a Tulajdonos és/vagy a 
Szellemi Tulajdon egyéb jogosultjai által.


### Használat



### Felelõsségi szabályok

Az Alkalmazáshoz kapcsolódó adatbázis módosítása kizárólag az Üzemeltetõ által, illetve az Alkalmazást üzemeltetõ webkiszolgálón keresztül
lehetséges. Bármilyen külsõ, nem az Alkalmazás részeként elérhetõ eszközzel történõ beavatkozás a Felhasználó azonnali kizárását eredményezi.

Ha a Felhasználó az Alkalmazást használat közben bezárja, vagy ha a kapcsolat (bármely okból) megszakad a kiszolgáló webhelyével,
abban az esetben az adatok elvesztéséért a Tulajdonos semmilyen felelõsséget nem vállal. A Tulajdonos és az Üzemeltetõ a rendelkezésére álló
eszközökkel biztosítja, hogy az Alkalmazás használata technikai szempontból biztonságosnak minõsüljön.

Az Alkalmazáshoz való csatlakozás miatt bekövetkezõ károkért, az internetes hálózat esetleges üzemkimaradásából, 
az elérési út hibájából, bármely nem várt technikai hibából eredõ adatvesztésért, vírusból, vagy más károkért a Tulajdonos nem felelõs. 
A Felhasználóknak minden esetben fel kell mérniük, hogy rendelkeznek-e az Alkalmazás használatához szükséges ismeretekkel, 
technikai követelményekkel és teljesítményekkel.
A Tulajdonos fenntartja magának a jogot arra, hogy amennyiben valamely Felhasználó részérõl bármilyen manipulációt, tömegesen generált letöltést,
illetve az Alkalmazás szellemével bármilyen módon összeférhetetlen vagy azt sértõ magatartást tapasztal, 
vagy ennek megalapozott gyanúja felmerül, úgy a Felhasználót azonnali hatállyal kizárja az Alkalmazás felhasználói körébõl.



### Technikai követelmények
Az Alkalmazás használatához szükséges technikai feltételek: Windows 10 operációs rendszer valamint minimum 400 MB szabad tárhely. 
A technikai feltételeket az Alkalmazás letöltéséhez és használatához a Felhasználónak kell teljesítenie. A technikai feltételek nem teljesüléséért a Tulajdonos nem vonható felelõsségre.
Ugyanígy nem vonható felelõsségre a Tulajdonos az Alkalmazás használatából a készüléken bekövetkezõ adatvesztésért, meghibásodásért. 
A Tulajdonos kizár minden kártérítési felelõsséget az Alkalmazáshoz csatlakozó minden külsõ szerver által nyújtott
vagy megjelenített adattal, információval kapcsolatban is.

Az Alkalmazás telepítéssel vehetõ használatba.


### Garancia és kártérítés

Az Alkalmazás használatához a felhasználói oldalon szükséges – fent meghatározott vagy bármely egyéb - technikai feltételeket a Felhasználónak kell biztosítania, teljesítenie.
Ezen technikai feltételek nem teljesüléséért a Tulajdonos nem vonható felelõsségre. Ugyanígy nem vonható felelõsségre a Tulajdonos az Alkalmazás használatából adódóan, 
a készüléken bekövetkezõ adatvesztésért, meghibásodásért. A Tulajdonos kizár minden kártérítési felelõsséget az Alkalmazáshoz csatlakozó minden külsõ szoftver által nyújtott
vagy megjelenített adattal, információval kapcsolatban. A Tulajdonos nem vállal garanciát az Alkalmazás megszakításmentes mûködéséért, 
valamint vis major hibákért. Az ebbõl eredõ adatvesztésért, tartalom vesztésért a Tulajdonos szintén nem tartozik kártérítési felelõsséggel.


### Egyéb rendelkezések

Jelen Felhasználási Feltételekben nem szabályozott kérdésekben a hatályos jogszabályok – különösen,
de nem kizárólagosan a Polgári Törvénykönyvrõl szóló 2013. évi V. törvény, az Európai Parlament és Tanács 2016. április 27-i (EU) 2016/679 Rendelete
a természetes személyeknek a személyes adatok kezelése tekintetében történõ védelmérõl és az ilyen adatok szabad áramlásáról, valamint a 95/46/EK 
irányelv hatályon kívül helyezésérõl, az információs önrendelkezési jogról és az információ szabadságról szóló 2011. évi CXII. törvény, a szerzõi jogról
szóló 1999. évi LXXVI. törvény, valamint az elektronikus kereskedelmi szolgáltatások, valamint az információs társadalommal összefüggõ szolgáltatások
egyes kérdéseirõl szóló 2001. évi CVIII. törvény – rendelkezései az irányadóak.

### Kapcsolat

Az Alkalmazás hosszútávú, megfelelõ mûködéséhez a szoftver üzemeltetését és támogatását a Fenntartó végzi munkanapokon, 8:00 és 16:00 között
Az Alkalmazás mûködésével kapcsolatban a fejlesztõk közösen ezen célra fenntartott e-mail címére
(továbbiakban: *NTBSLHK@gmail.com*) várjuk a szolgáltatással kapcsolatosan felmerülõ kérdéseit, tapasztalatait.
A Fenntartó igyekszik a fentebb említett idõszakban a kérdéseket kielégítõen megválaszolni.
A változtatás joga és lehetõsége fejlesztés révén abszolút módon fennáll.

### Jelenlegi üzleti folyamatok

Jelenlegi helyzetünk, nevezetesen a járványhelyzet valamint a korábbi oktatási modellek hiányosságai
újabb digitalizációs lépésekre sarkallják a felsõoktatási szférát is. Ezen információ értelmében szükségeltetik
egy olyan webhely felépítése, amelyen keresztül biztosítjuk a hallgatók a gyakorlatokhoz elvárt, 
megfelelõ szintû és nyelvezetû tananyaghoz, továbbá a gyakorlatban felmerülõ feladatokhoz való hozzáférését.
A megrendelõ fontosnak tartja továbbá, hogy a diákok visszajelzéseket kapjanak a feladatokhoz csatolt megoldásaikhoz.

### Igényelt üzleti folyamatok

Fent említett okokból következõen cégünknek is haladnia kell jelen korunk egyre növekvõ elvárásaival, 
és ezáltal szükséges lépéssé vált egy jól funkcionáló feladatkiosztó rendszer kiépítése.
Ezalatt egy online webes felületet értünk, amelynek segítségével lehetõséget kapnak 
az intézmény tanárai egy szerveren tárolt adatbázisba kigyûjteni a hallgatóknak szánt feladatok részleteit.

### Fogalomtár
	- Grafikus felhasználói felület - GUI: a számítógép és ember közti kapcsolatot megvalósító elemek összessége. 
	- weboldal: gyakorlatilag az interneten található, hipertext dokumentum, amelyet valamilyen böngészõprogrammal lehet megjeleníteni. Tartalmaz különbözõ objektumokat: képeket, szöveget, táblázatokat, hivatkozásokat más weboldalakra stb. 
	A webböngészõ ezen adathalmazra fogalmaz meg egy úgynevezett HTTP-GET-kérést, ami azt eredményezi, hogy a böngészõ felületén megjelenik a lekérdezett weboldal a leírónyelvû dokumentum (html - css) alapján megfelelõen formázva.
	- adatbázis: azonos minõségû, megfelelõen strukturált diszkrét adatok összessége, amelyet egy azok tárolására, lekérdezésére és módosítására különbözõ adatbázis-kezelõ szoftvereket használunk. 
	Célja az adatok megbízható, perzisztens tárolása és viszonylag/kellõen gyors lekérdezhetõségének biztosítása.