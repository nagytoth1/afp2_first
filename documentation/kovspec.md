# Követelmény specifikáció

### Áttekintés



### Jelenlegi helyzet



### Vágyálomrendszer

	- Tudjuk nyomon követni a rendszeridőt (naplózás és a hallgatók időbeli igazodása szempontjából fontos)
	- 45 percenként figyelmeztessen (hallgató álljon fel a géptől, mozogjon)
	- Jó lenne, ha adatbázis-kapcsolatot használhatnánk a későbbiekben a feladatra adott válaszok pontszámainak tárolására 
	(a session idejére).
	- Jó lenne, ha meg tudnánk nézni a weboldal látogatásainak időpontjait naplózás szempontjából.
	- Szeretnénk, hogy az weboldal gördülékenyen reagáljon, legyen reszponzív.
	- Az adatbázis legyen egy internetes repozitóriumból elérhető

### Elvárások


## Követelménylista

|    Modul    	| ID |       Név        	|                                                        Kifejtés                                                       		|
|-------------	|----|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Interface   	| I1 | Menüsor   		| Ne legyen túlgondolva, a PTI-s tárgyak legyenek kilistázva, ezekre kattintva átvisz a megfelelő oldal feladatlistájára. 		|
| Interface	| I2 | Felhasználói felület	| A teljes felhasználói felület legyen leegyszerűsített, minimalista.									|
| Interface 	| I3 | Egyéb hivatkozások      	| Legyenek hivatkozások a suli honlapjára, Neptun-oldalára, az e-learning-oldalra							|
| Interface	| I4 | Feladatkiosztó		| A feladatok sablonjait töltsük ki az adatbázisból olvasott adatokkal.									|
| Datastore 	| D1 | Adattárolási mód 	| Egy adatbázis-táblában eltároljuk a különböző tárgyakhoz kapcsolódó feladatok részleteit, ezek megfelelő helyekre beollózva.		|
| Datastore 	| D2 | Tervezett karbantartás	| A feladatok adatbázisa félévek kezdete előtti héten legyen takarítva, lehetőleg inkább egyre bővebb készlet álljon rendelkezésre.	|
| Datastore 	| D3 | Adatbázis        	| Tároljuk az adatokat adatbázisban, szerkezete legyen a lehető legegyszerűbb, mivel sok feladat részleteit fogunk tárolni. 		|
| Feature   	| F1 | Rendszeridő      	| Mutasson rendszeridőt a képernyő valamely, a munka szempontjából kevésbé zavaró részén.						|
| Feature   	| F2 | Random adatolvasás      	| Az adatbázisból olvassunk ki véletlenszerűen egy rekordot (egy feladat-csomagot) a tárgynak megfelelő rekeszekből.			|

### Rendszerre vonatkozó törvények

**Kivonat: 18/2018. (V. 31.) utasítás az Informatikai Biztonsági Szabályzatról**
	<p>	*171.* 	Az operációs rendszer, az alkalmazás és a hálózati aktív eszköz szoftver verzióját, valamint biztonsági patch szintjét tesztelést követően lehetőség szerint a gyártói támogatással rendelkező, legmagasabb szintre kell hozni.(…) </p>
	<p>	*177.* 	Meglévő rendszer esetén a biztonságot közvetlenül veszélyeztető hibákat a lehető leghamarabb javítani kell, vagy korrektív kontroll alkalmazásával csökkenteni a kockázatokat. Új rendszer esetén feltárt sérülékenységet a használatbavételig javítani kell. </p>
	<p>	*178.* 	A hálózatok ki- és bemeneteli pontjait minimalizálni kell, továbbá a ki- és bemeneti pontok adatforgalmát elektronikusan naplózni, és a naplófájlokat ellenőrizni kell.</p>
	<p>	*179.* 	Az informatikai üzemeltetésért felelős vezetőnek a rendszer minden arra alkalmas – megfelelő hardver- és szoftverkörnyezettel rendelkező – elemére jóváhagyott, központilag rendszeresített vírusellenőrző szoftvert kell telepítenie és naprakészen tartania.(…)</p>
	<p>	*183.* 	A biztonsági mentés célja az információ és az adatfeldolgozó szoftverek épségének és rendelkezésre állásának biztosítása. A hatékony biztonsági adatmentés érdekében a munkaállomásokon feldolgozott adatállományokat tárolni kizárólag szervereken és központi kiszolgálókon, valamint az adatmentésre szolgáló médián lehet. Bármilyen más helyen történő adattárolás még átmenetileg is tilos.(…)</p>
	<p>	*200.* 	Tilos a hálózat biztonságos működését zavaró vagy veszélyeztető információk, programok terjesztése. (…)</p>
	<p>	*208.* 	A rendszert és a hálózatot túlterheléses – szolgáltatás megtagadás jellegű – támadásokkal szembeni védelemmel kell ellátni.(…)</p>
	<p>	*222.* 	A fejlesztés során a biztonságos programozás irányelveit kell követni. A szoftverfejlesztés során a szoftver funkcionalitása mellett fokozott figyelmet kell fordítani a rendszer és a kapcsolódó rendszerek biztonsági követelményeinek betartására is.</p>
	<p>	*forrás: NJT* </p>

#### Szerzői jogok
**Kivonat az 1999. évi LXXVI. szerzői jogi törvényből:**
	<p>*1.§* 	(2) Szerzői jogi védelem alá tartozik – függetlenül attól, hogy e törvény megnevezi-e – 
				az irodalom, a tudomány és a művészet minden alkotása. Ilyen alkotásnak minősül különösen: (...)</p>
			<p>&emsp; &emsp;c) a *számítógépi programalkotás és a hozzá tartozó dokumentáció (a továbbiakban: szoftver) akár forráskódban, akár tárgykódban vagy bármilyen más formában* rögzített minden fajtája, ideértve a felhasználói programot és az operációs rendszert is.(...)</p>
			<p>&emsp;(3) A szerzői jogi védelem az alkotást a szerző szellemi tevékenységéből fakadó egyéni, eredeti jellege alapján illeti meg. A védelem nem függ mennyiségi, minőségi, esztétikai jellemzőktől vagy az alkotás színvonalára vonatkozó értékítélettől. (...)</p>
	<p>*4.$* (1) A szerzői jog *azt illeti, aki a művet megalkotta* (szerző). </p>
			<p>&emsp;(2) *Szerzői jogi védelem* alatt áll – az eredeti mű szerzőjét megillető jogok sérelme nélkül – más szerző művének átdolgozása, feldolgozása vagy fordítása is, ha annak egyéni, eredeti jellege van.(...)</p>
	<p>*5.§* (1) Több szerző közös művére, ha annak részei nem használhatók fel önállóan, a szerzői jog együttesen és – kétség esetén – egyenlő arányban illeti meg a szerzőtársakat; a szerzői jog megsértése ellen azonban bármelyik szerzőtárs önállóan is felléphet. (...)</p>
	<p>*13.§* A szerző személyhez fűződő jogát sérti művének a becsületére vagy jóhírnevére sérelmes mindenfajta eltorzítása, megcsonkítása, megváltoztatása és a művel kapcsolatos más ilyen jellegű visszaélés.(...)</p>
	<p>*42.§* (1) Felhasználási szerződés alapján a szerző engedélyt ad művének a felhasználására, a felhasználó pedig köteles ennek fejében díjat fizetni. (...)</p>
	<p>*59.§* (1) Eltérő megállapodás hiányában a szerző kizárólagos joga nem terjed ki a többszörözésre, az átdolgozásra, a feldolgozásra, a fordításra, a szoftver bármely más módosítására – ideértve a hiba kijavítását is –, valamint ezek eredményének többszörözésére annyiban, amennyiben e felhasználási cselekményeket a szoftvert jogszerűen megszerző személy a szoftver rendeltetésével összhangban végzi.</p>
			<p>&emsp;(2) A felhasználási szerződésben sem zárható ki, hogy a felhasználó egy biztonsági másolatot készíthessen a szoftverről, ha az a felhasználáshoz szükséges.</p>
			<p>&emsp;(3) Aki a szoftver valamely példányának felhasználására jogosult, a szerző engedélye nélkül is megfigyelheti és tanulmányozhatja a szoftver működését, továbbá kipróbálhatja a szoftvert annak betáplálása, képernyőn való megjelenítése, futtatása, továbbítása vagy tárolása során abból a célból, hogy a szoftver valamely elemének alapjául szolgáló elgondolást vagy elvet megismerje.</p>
<p>(Forrás: NJT)</p>

### Általános Információk

Az Alkalmazásnak a használatát és a hozzáférését megelőzi az alkalmazandó jogszabályok és a jelen Felhasználási Feltételek
és Adatkezelési tájékoztatóknak az elolvasása és értelmezése. Amennyiben az alkalmazást letöltők vagy használók (a későbbiekben: a Felhasználók)
elfogadják és teljesítik az imént említett Felhasználási Feltételeket abban az esetben az alkalmazás használata engedélyezett. Amennyiben ezen
Adatkezelési Tájékoztatót és a Felhasználói Feltételek nem fogadják el, abban az esetben a Felhasználó nem jogosult arra hogy az alkalmazást használhassa.

A jelenlegi Felhasználási Feltételekre a magyar jog az irányadó, tekintet nélkül a nemzetközi magánjog előírásaira. Az Alkalmazás Felhasználói
kifejezetten hozzájárulnak ahhoz, hogy a jogvitákra a magyar hatóságoknak és bíróságoknak legyen kizárólags joghatóságuk a magyar jog alapján.

### Szellemi tulajdon

Az Alkalmazás és valamennyi kapcsolódó védjegy, szerzői jogi alkotás és egyéb - akár bejegyzett, akár be nem jegyzett - szellemi tulajdon
(a továbbiakban együttesen: Szellemi Tulajdon) tulajdonosa az EKE és/vagy EKE Szolgáltató, valamint az alkalmazáshoz kedvezményt nyújtó
partnerek. A Felhasználók az Alkalmazást a Szellemi Tulajdon maximális tiszteletben tartásával jogosultak használni. 

A Szellemi Tulajdon kiterjed különösen, de nem kizárólagosan valamennyi szoftverre, logóra, márkajelre, márkanévre, fényképre, szövegre, grafikára, adatbázisra.
A Szellemi Tulajdonnak tilos bárminemű megsértése, bitorlása, másolása, átdolgozása és tilos azt bármilyen egyéb módon megsérteni,
azt jogosulatlanul felhasználni, továbbadni, megterhelni, azzal bármilyen módon rendelkezni, visszaélni. 

Ezen szabályok megsértése az Alkalmazás használati lehetőségeinek azonnali hatályú megszüntetése mellett a megfelelő jogi lépések megtételét
– beleértve esetleges büntetőjogi lépések megtételét is – vonja maga után a Felhasználóval, más jogsértő személlyel szemben a Tulajdonos és/vagy a 
Szellemi Tulajdon egyéb jogosultjai által.


### Használat



### Felelősségi szabályok

Az Alkalmazáshoz kapcsolódó adatbázis módosítása kizárólag az Üzemeltető által, illetve az Alkalmazást üzemeltető webkiszolgálón keresztül
lehetséges. Bármilyen külső, nem az Alkalmazás részeként elérhető eszközzel történő beavatkozás a Felhasználó azonnali kizárását eredményezi.

Ha a Felhasználó az Alkalmazást használat közben bezárja, vagy ha a kapcsolat (bármely okból) megszakad a kiszolgáló webhelyével,
abban az esetben az adatok elvesztéséért a Tulajdonos semmilyen felelősséget nem vállal. A Tulajdonos és az Üzemeltető a rendelkezésére álló
eszközökkel biztosítja, hogy az Alkalmazás használata technikai szempontból biztonságosnak minősüljön.

Az Alkalmazáshoz való csatlakozás miatt bekövetkező károkért, az internetes hálózat esetleges üzemkimaradásából, 
az elérési út hibájából, bármely nem várt technikai hibából eredő adatvesztésért, vírusból, vagy más károkért a Tulajdonos nem felelős. 
A Felhasználóknak minden esetben fel kell mérniük, hogy rendelkeznek-e az Alkalmazás használatához szükséges ismeretekkel, 
technikai követelményekkel és teljesítményekkel.
A Tulajdonos fenntartja magának a jogot arra, hogy amennyiben valamely Felhasználó részéről bármilyen manipulációt, tömegesen generált letöltést,
illetve az Alkalmazás szellemével bármilyen módon összeférhetetlen vagy azt sértő magatartást tapasztal, 
vagy ennek megalapozott gyanúja felmerül, úgy a Felhasználót azonnali hatállyal kizárja az Alkalmazás felhasználói köréből.



### Technikai követelmények
Az Alkalmazás használatához szükséges technikai feltételek: Windows 10 operációs rendszer valamint minimum 400 MB szabad tárhely. 
A technikai feltételeket az Alkalmazás letöltéséhez és használatához a Felhasználónak kell teljesítenie. A technikai feltételek nem teljesüléséért a Tulajdonos nem vonható felelősségre.
Ugyanígy nem vonható felelősségre a Tulajdonos az Alkalmazás használatából a készüléken bekövetkező adatvesztésért, meghibásodásért. 
A Tulajdonos kizár minden kártérítési felelősséget az Alkalmazáshoz csatlakozó minden külső szerver által nyújtott
vagy megjelenített adattal, információval kapcsolatban is.

Az Alkalmazás telepítéssel vehető használatba.


### Garancia és kártérítés

Az Alkalmazás használatához a felhasználói oldalon szükséges – fent meghatározott vagy bármely egyéb - technikai feltételeket a Felhasználónak kell biztosítania, teljesítenie.
Ezen technikai feltételek nem teljesüléséért a Tulajdonos nem vonható felelősségre. Ugyanígy nem vonható felelősségre a Tulajdonos az Alkalmazás használatából adódóan, 
a készüléken bekövetkező adatvesztésért, meghibásodásért. A Tulajdonos kizár minden kártérítési felelősséget az Alkalmazáshoz csatlakozó minden külső szoftver által nyújtott
vagy megjelenített adattal, információval kapcsolatban. A Tulajdonos nem vállal garanciát az Alkalmazás megszakításmentes működéséért, 
valamint vis major hibákért. Az ebből eredő adatvesztésért, tartalom vesztésért a Tulajdonos szintén nem tartozik kártérítési felelősséggel.


### Egyéb rendelkezések

Jelen Felhasználási Feltételekben nem szabályozott kérdésekben a hatályos jogszabályok – különösen,
de nem kizárólagosan a Polgári Törvénykönyvről szóló 2013. évi V. törvény, az Európai Parlament és Tanács 2016. április 27-i (EU) 2016/679 Rendelete
a természetes személyeknek a személyes adatok kezelése tekintetében történő védelméről és az ilyen adatok szabad áramlásáról, valamint a 95/46/EK 
irányelv hatályon kívül helyezéséről, az információs önrendelkezési jogról és az információ szabadságról szóló 2011. évi CXII. törvény, a szerzői jogról
szóló 1999. évi LXXVI. törvény, valamint az elektronikus kereskedelmi szolgáltatások, valamint az információs társadalommal összefüggő szolgáltatások
egyes kérdéseiről szóló 2001. évi CVIII. törvény – rendelkezései az irányadóak.

### Kapcsolat

Az Alkalmazás hosszútávú, megfelelő működéséhez a szoftver üzemeltetését és támogatását a Fenntartó végzi munkanapokon, 8:00 és 16:00 között
Az Alkalmazás működésével kapcsolatban a fejlesztők közösen ezen célra fenntartott e-mail címére
(továbbiakban: *NTBSLHK@gmail.com*) várjuk a szolgáltatással kapcsolatosan felmerülő kérdéseit, tapasztalatait.
A Fenntartó igyekszik a fentebb említett időszakban a kérdéseket kielégítően megválaszolni.
A változtatás joga és lehetősége fejlesztés révén abszolút módon fennáll.

### Jelenlegi üzleti folyamatok

Jelenlegi helyzetünk, nevezetesen a járványhelyzet valamint a korábbi oktatási modellek hiányosságai
újabb digitalizációs lépésekre sarkallják a felsőoktatási szférát is. Ezen információ értelmében szükségeltetik
egy olyan webhely felépítése, amelyen keresztül biztosítjuk a hallgatók a gyakorlatokhoz elvárt, 
megfelelő szintű és nyelvezetű tananyaghoz, továbbá a gyakorlatban felmerülő feladatokhoz való hozzáférését.
A megrendelő fontosnak tartja továbbá, hogy a diákok visszajelzéseket kapjanak a feladatokhoz csatolt megoldásaikhoz.

### Igényelt üzleti folyamatok

Fent említett okokból következően cégünknek is haladnia kell jelen korunk egyre növekvő elvárásaival, 
és ezáltal szükséges lépéssé vált egy jól funkcionáló feladatkiosztó rendszer kiépítése.
Ezalatt egy online webes felületet értünk, amelynek segítségével lehetőséget kapnak 
az intézmény tanárai egy szerveren tárolt adatbázisba kigyűjteni a hallgatóknak szánt feladatok részleteit.

### Fogalomtár
	- Grafikus felhasználói felület - GUI: a számítógép és ember közti kapcsolatot megvalósító elemek összessége. 
	- weboldal: gyakorlatilag az interneten található, hipertext dokumentum, amelyet valamilyen böngészőprogrammal lehet megjeleníteni. Tartalmaz különböző objektumokat: képeket, szöveget, táblázatokat, hivatkozásokat más weboldalakra stb. 
	A webböngésző ezen adathalmazra fogalmaz meg egy úgynevezett HTTP-GET-kérést, ami azt eredményezi, hogy a böngésző felületén megjelenik a lekérdezett weboldal a leírónyelvű dokumentum (html - css) alapján megfelelően formázva.
	- adatbázis: azonos minőségű, megfelelően strukturált diszkrét adatok összessége, amelyet egy azok tárolására, lekérdezésére és módosítására különböző adatbázis-kezelő szoftvereket használunk. 
	Célja az adatok megbízható, perzisztens tárolása és viszonylag/kellően gyors lekérdezhetőségének biztosítása.
	