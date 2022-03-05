# Funkcionális specifikáció

### Áttekintés

A funkcionális specifikáció	folyamán előzetesen is definiáljuk,
hogy konkrétan milyen célokra, milyen felhasználási területre készítjük a terméket, 
az általunk fejlesztett szoftvert. A követelményspecifikációban lefektetett 
kritériumoknak megfeleltetjük a szoftver jövőbeli funkcióit, ezeket természetesen 
kötelességünknek érezzük a megrendelő személy(ek) tudtára is adni.
Ezek alapján a megrendelő képes lesz saját legjobb belátása szerint eldönteni,
szerződik-e kis csapatunkkal a termék kidolgozásának, tesztelési fázisának, 
végül annak értékesítésének, átadásának idejére, avagy mégsem tart igényt szolgáltatásunkra.


### Vágyálomrendszer

	- Kell egy adatbázis a háttéradatoknak
	- Ez az adatbázis egy online szerverre, egy felhőre kell, hogy kerüljön, ugyanis a cégnek nincs fizikai szerverbázisa.
	- Adatbázis implementációja
	- Az adatbázis tárolja a következőket:
		- 	tárgyakat(ezeknek a nevét,tárgykódját, férőhely stb),
		- 	hallgatókat(Neptun_kód,Név,Jelszó,Idegen kulcsként hogy melyik tárgyhoz illetve tanárhoz tartozik)
		- 	tanárokat(Neptun_kód,Név,Jelszót nem szükséges eltárolni tanárhoz)
	- Weboldalhoz -> Laravelt, illetve az adatbázishoz SQLite/MySQL lesz használva
	- Felhasználói funkciók: 
		- Bejelentkező felület, regisztráció nem kell, mivel a rendszerben már megvan az összes hallgatónak a Neptun kódja és a jelszava is.
		- A jelszó változtatásra lehetőség van.
		- Tárgyak listáját illetve ezeknek az anyagait eltudja érni.
		- Különféle házifeladatokat lehet kitölteni, anyagok megnyitása révén.
		- Tanárokat adatlapjait is meglehet tekinteni.

	
### Elvárások

Egy Online tanuló weboldal amelybe kötelező a bejelentkezés. Emellett a tárgyakat ki lehet listázni, és minden tanulóhoz
tárgyai szerint tud feladatokat megoldani akár gyakorlásképpen akár mint kötelező feladat. 

### A rendszer céljai és nem céljai

Célok:
	- Egy olyan weboldal létrehozása amely segít a hallgatónak az órára való felkészülésre és a tárgynak a teljesítésére.
	- A felület live-track-eli (valós időben frissíti) a bejelentkezést egy adott tanulónak.
	- Tiszta és áttekinthető felület létrehozása, zavaró/elterelő tényezők nélkül.
	- Legördülő menüsor a tárgyakhoz feladatokat rendel mint házifeladat mint gyakorlófeladat képpen.
	- Kínál egy bejelentkező felületet.
	- Felületnek reszponzívnak kell lennie.
Nem célok:
	- A fentebb felsoroltakon kívül az alkalmazás nem kínál extra funkciókat.

### Jelenlegi üzleti folyamatok modellje

A követelményspecifikációban kifejtett elvek teljes mértékben érvényesülnek ezen dokumentum soraiban is.
A redundancia elkerülésének céljából ez a fejezet szimplán csak a követelményspecifikáció kapcsolódó fejezetére való referenciaként készült.
A megfelelő sorok megtalálhatók a másik dokumentum ugyanezen elnevezésű fejezetében,
kérem a kedves olvasót, hogy az erre vonatkozó résszel ott ismerkedjen meg.
(referencia: Jelenlegi üzleti folyamatok, 176.sortól kezdődően)


### Igényelt üzleti folyamatok modellje

A követelményspecifikációban kifejtett elvek teljes mértékben érvényesülnek ezen dokumentum soraiban is.
A redundancia elkerülése végett ez a fejezet szimplán csak egy referencia a követelményspecifikáció kapcsolódó fejezetére.
A megfelelő sorok megtalálhatók a másik dokumentum ugyanezen elnevezésű fejezetében,
kérem a kedves olvasót, hogy az erre vonatkozó résszel ott ismerkedjen meg.
(referencia: Igényelt üzleti folyamatok, 185.sortól kezdődően)


### Követelménylista

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
							 								|


### Használati esetek (use-case)

A hallgatónak elsőnek be kell jelentkezni amennyiben tudatában van a rendszernek a validáló adataival 
abban az esetben a belépés engedélyezett, amennyiben nem tudja ezeket az adatok a rendszer nem engedi tovább.
Amennyiben a belépés sikeres volt a rendszer azonnal megjeleníti számára a weboldal összes funkcióit.
Belépést követően a hallgató számára láthatóvá lesz az üdvözlő oldal ahol általános információkat illetve navigációt kínál fel.
Ezek után a fejlécben megtalálható menüsor alapján tud tovább navigálni a hallgató. Amennyiben kiválasztja a Tárgyak menüpontot,
előtárul a hallgató számára az összes tárgy, ezek közül csak azokat tudja majd megnyitni a hallgató amelyekre fel van jelentkeztetve
a tanár által. Ezután adott tárgyra kattintva elkezdheti a gyakorlófeladatok illetve a tananyag megtekintését. Kilépési funkcióra van lehetőség.

### Képernyő tervek

#TODO!!!

### Fogalomtár
	- Neptun kód: Egy adott hallgatóhoz rendelt egyedi 6 egységből álló hexadecimális érték amelyet a rendszer randomizálva oszt ki.  
	- Grafikus felhasználói felület - GUI: a számítógép és ember közti kapcsolatot megvalósító elemek összessége. 
	- weboldal: gyakorlatilag az interneten található, hipertext dokumentum, amelyet valamilyen böngészőprogrammal lehet megjeleníteni. Tartalmaz különböző objektumokat: képeket, szöveget, táblázatokat, hivatkozásokat más weboldalakra stb. 
	A webböngésző ezen adathalmazra fogalmaz meg egy úgynevezett HTTP-GET-kérést, ami azt eredményezi, hogy a böngésző felületén megjelenik a lekérdezett weboldal a leírónyelvű dokumentum (html - css) alapján megfelelően formázva.
	- adatbázis: azonos minőségű, megfelelően strukturált diszkrét adatok összessége, amelyet egy azok tárolására, lekérdezésére és módosítására különböző adatbázis-kezelő szoftvereket használunk. 
	Célja az adatok megbízható, perzisztens tárolása és viszonylag/kellően gyors lekérdezhetőségének biztosítása.