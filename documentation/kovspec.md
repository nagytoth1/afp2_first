# K�vetelm�ny specifik�ci�

### �ttekint�s



### Jelenlegi helyzet



### V�gy�lomrendszer

	- Tudjuk nyomon k�vetni a rendszerid�t (napl�z�s �s a hallgat�k id�beli igazod�sa szempontj�b�l fontos)
	- 45 percenk�nt figyelmeztessen (hallgat� �lljon fel a g�pt�l, mozogjon)
	- J� lenne, ha adatb�zis-kapcsolatot haszn�lhatn�nk a k�s�bbiekben a feladatra adott v�laszok pontsz�mainak t�rol�s�ra (a session idej�re).
	- J� lenne, ha meg tudn�nk n�zni a weboldal l�togat�sainak id�pontjait napl�z�s szempontj�b�l.
	- Szeretn�nk, hogy az weboldal g�rd�l�kenyen reag�ljon, legyen reszponz�v.
	- Az adatb�zis legyen egy internetes repozit�riumb�l el�rhet�

### Elv�r�sok


## K�vetelm�nylista

|    Modul    	| ID |       N�v        	|                                                        Kifejt�s                                                       		|
|-------------	|----|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Interface   	| I1 | Men�sor   		| Ne legyen t�lgondolva, a PTI-s t�rgyak legyenek kilist�zva, ezekre kattintva �tvisz a megfelel� oldal feladatlist�j�ra. 		|
| Interface	| I2 | Felhaszn�l�i fel�let	| A teljes felhaszn�l�i fel�let legyen leegyszer�s�tett, minimalista.									|
| Interface 	| I3 | Egy�b hivatkoz�sok      	| Legyenek hivatkoz�sok a suli honlapj�ra, Neptun-oldal�ra, az e-learning-oldalra							|
| Interface	| I4 | Feladatkioszt�		| A feladatok sablonjait t�lts�k ki az adatb�zisb�l olvasott adatokkal.									|
| Datastore 	| D1 | Adatt�rol�si m�d 	| Egy adatb�zis-t�bl�ban elt�roljuk a k�l�nb�z� t�rgyakhoz kapcsol�d� feladatok r�szleteit, ezek megfelel� helyekre beoll�zva.		|
| Datastore 	| D2 | Tervezett karbantart�s	| A feladatok adatb�zisa f�l�vek kezdete el�tti h�ten legyen takar�tva, lehet�leg ink�bb egyre b�vebb k�szlet �lljon rendelkez�sre.	|
| Datastore 	| D3 | Adatb�zis        	| T�roljuk az adatokat adatb�zisban, szerkezete legyen a lehet� legegyszer�bb, mivel sok feladat r�szleteit fogunk t�rolni. 		|
| Feature   	| F1 | Rendszerid�      	| Mutasson rendszerid�t a k�perny� valamely, a munka szempontj�b�l kev�sb� zavar� r�sz�n.						|
| Feature   	| F2 | Random adatolvas�s      	| Az adatb�zisb�l olvassunk ki v�letlenszer�en egy rekordot (egy feladat-csomagot) a t�rgynak megfelel� rekeszekb�l.			|

### Rendszerre vonatkoz� t�rv�nyek

**Kivonat: 18/2018. (V. 31.) utas�t�s az Informatikai Biztons�gi Szab�lyzatr�l**
	<p>	*171.* 	Az oper�ci�s rendszer, az alkalmaz�s �s a h�l�zati akt�v eszk�z szoftver verzi�j�t, valamint biztons�gi patch szintj�t tesztel�st k�vet�en lehet�s�g szerint a gy�rt�i t�mogat�ssal rendelkez�, legmagasabb szintre kell hozni.(�) </p>
	<p>	*177.* 	Megl�v� rendszer eset�n a biztons�got k�zvetlen�l vesz�lyeztet� hib�kat a lehet� leghamarabb jav�tani kell, vagy korrekt�v kontroll alkalmaz�s�val cs�kkenteni a kock�zatokat. �j rendszer eset�n felt�rt s�r�l�kenys�get a haszn�latbav�telig jav�tani kell. </p>
	<p>	*178.* 	A h�l�zatok ki- �s bemeneteli pontjait minimaliz�lni kell, tov�bb� a ki- �s bemeneti pontok adatforgalm�t elektronikusan napl�zni, �s a napl�f�jlokat ellen�rizni kell.</p>
	<p>	*179.* 	Az informatikai �zemeltet�s�rt felel�s vezet�nek a rendszer minden arra alkalmas � megfelel� hardver- �s szoftverk�rnyezettel rendelkez� � elem�re j�v�hagyott, k�zpontilag rendszeres�tett v�rusellen�rz� szoftvert kell telep�tenie �s naprak�szen tartania.(�)</p>
	<p>	*183.* 	A biztons�gi ment�s c�lja az inform�ci� �s az adatfeldolgoz� szoftverek �ps�g�nek �s rendelkez�sre �ll�s�nak biztos�t�sa. A hat�kony biztons�gi adatment�s �rdek�ben a munka�llom�sokon feldolgozott adat�llom�nyokat t�rolni kiz�r�lag szervereken �s k�zponti kiszolg�l�kon, valamint az adatment�sre szolg�l� m�di�n lehet. B�rmilyen m�s helyen t�rt�n� adatt�rol�s m�g �tmenetileg is tilos.(�)</p>
	<p>	*200.* 	Tilos a h�l�zat biztons�gos m�k�d�s�t zavar� vagy vesz�lyeztet� inform�ci�k, programok terjeszt�se. (�)</p>
	<p>	*208.* 	A rendszert �s a h�l�zatot t�lterhel�ses � szolg�ltat�s megtagad�s jelleg� � t�mad�sokkal szembeni v�delemmel kell ell�tni.(�)</p>
	<p>	*222.* 	A fejleszt�s sor�n a biztons�gos programoz�s ir�nyelveit kell k�vetni. A szoftverfejleszt�s sor�n a szoftver funkcionalit�sa mellett fokozott figyelmet kell ford�tani a rendszer �s a kapcsol�d� rendszerek biztons�gi k�vetelm�nyeinek betart�s�ra is.</p>
	<p>	*forr�s: NJT* </p>

#### Szerz�i jogok
**Kivonat az 1999. �vi LXXVI. szerz�i jogi t�rv�nyb�l:**
	<p>*1.�* 	(2) Szerz�i jogi v�delem al� tartozik � f�ggetlen�l att�l, hogy e t�rv�ny megnevezi-e � 
				az irodalom, a tudom�ny �s a m�v�szet minden alkot�sa. Ilyen alkot�snak min�s�l k�l�n�sen: (...)</p>
			<p>&emsp; &emsp;c) a *sz�m�t�g�pi programalkot�s �s a hozz� tartoz� dokument�ci� (a tov�bbiakban: szoftver) ak�r forr�sk�dban, ak�r t�rgyk�dban vagy b�rmilyen m�s form�ban* r�gz�tett minden fajt�ja, ide�rtve a felhaszn�l�i programot �s az oper�ci�s rendszert is.(...)</p>
			<p>&emsp;(3) A szerz�i jogi v�delem az alkot�st a szerz� szellemi tev�kenys�g�b�l fakad� egy�ni, eredeti jellege alapj�n illeti meg. A v�delem nem f�gg mennyis�gi, min�s�gi, eszt�tikai jellemz�kt�l vagy az alkot�s sz�nvonal�ra vonatkoz� �rt�k�t�lett�l. (...)</p>
	<p>*4.$* (1) A szerz�i jog *azt illeti, aki a m�vet megalkotta* (szerz�). </p>
			<p>&emsp;(2) *Szerz�i jogi v�delem* alatt �ll � az eredeti m� szerz�j�t megillet� jogok s�relme n�lk�l � m�s szerz� m�v�nek �tdolgoz�sa, feldolgoz�sa vagy ford�t�sa is, ha annak egy�ni, eredeti jellege van.(...)</p>
	<p>*5.�* (1) T�bb szerz� k�z�s m�v�re, ha annak r�szei nem haszn�lhat�k fel �n�ll�an, a szerz�i jog egy�ttesen �s � k�ts�g eset�n � egyenl� ar�nyban illeti meg a szerz�t�rsakat; a szerz�i jog megs�rt�se ellen azonban b�rmelyik szerz�t�rs �n�ll�an is fell�phet. (...)</p>
	<p>*13.�* A szerz� szem�lyhez f�z�d� jog�t s�rti m�v�nek a becs�let�re vagy j�h�rnev�re s�relmes mindenfajta eltorz�t�sa, megcsonk�t�sa, megv�ltoztat�sa �s a m�vel kapcsolatos m�s ilyen jelleg� vissza�l�s.(...)</p>
	<p>*42.�* (1) Felhaszn�l�si szerz�d�s alapj�n a szerz� enged�lyt ad m�v�nek a felhaszn�l�s�ra, a felhaszn�l� pedig k�teles ennek fej�ben d�jat fizetni. (...)</p>
	<p>*59.�* (1) Elt�r� meg�llapod�s hi�ny�ban a szerz� kiz�r�lagos joga nem terjed ki a t�bbsz�r�z�sre, az �tdolgoz�sra, a feldolgoz�sra, a ford�t�sra, a szoftver b�rmely m�s m�dos�t�s�ra � ide�rtve a hiba kijav�t�s�t is �, valamint ezek eredm�ny�nek t�bbsz�r�z�s�re annyiban, amennyiben e felhaszn�l�si cselekm�nyeket a szoftvert jogszer�en megszerz� szem�ly a szoftver rendeltet�s�vel �sszhangban v�gzi.</p>
			<p>&emsp;(2) A felhaszn�l�si szerz�d�sben sem z�rhat� ki, hogy a felhaszn�l� egy biztons�gi m�solatot k�sz�thessen a szoftverr�l, ha az a felhaszn�l�shoz sz�ks�ges.</p>
			<p>&emsp;(3) Aki a szoftver valamely p�ld�ny�nak felhaszn�l�s�ra jogosult, a szerz� enged�lye n�lk�l is megfigyelheti �s tanulm�nyozhatja a szoftver m�k�d�s�t, tov�bb� kipr�b�lhatja a szoftvert annak bet�pl�l�sa, k�perny�n val� megjelen�t�se, futtat�sa, tov�bb�t�sa vagy t�rol�sa sor�n abb�l a c�lb�l, hogy a szoftver valamely elem�nek alapj�ul szolg�l� elgondol�st vagy elvet megismerje.</p>
<p>(Forr�s: NJT)</p>

### �ltal�nos Inform�ci�k

Az Alkalmaz�snak a haszn�lat�t �s a hozz�f�r�s�t megel�zi az alkalmazand� jogszab�lyok �s a jelen Felhaszn�l�si Felt�telek
�s Adatkezel�si t�j�koztat�knak az elolvas�sa �s �rtelmez�se. Amennyiben az alkalmaz�st let�lt�k vagy haszn�l�k (a k�s�bbiekben: a Felhaszn�l�k)
elfogadj�k �s teljes�tik az im�nt eml�tett Felhaszn�l�si Felt�teleket abban az esetben az alkalmaz�s haszn�lata enged�lyezett. Amennyiben ezen
Adatkezel�si T�j�koztat�t �s a Felhaszn�l�i Felt�telek nem fogadj�k el, abban az esetben a Felhaszn�l� nem jogosult arra hogy az alkalmaz�st haszn�lhassa.

A jelenlegi Felhaszn�l�si Felt�telekre a magyar jog az ir�nyad�, tekintet n�lk�l a nemzetk�zi mag�njog el��r�saira. Az Alkalmaz�s Felhaszn�l�i
kifejezetten hozz�j�rulnak ahhoz, hogy a jogvit�kra a magyar hat�s�goknak �s b�r�s�goknak legyen kiz�r�lags joghat�s�guk a magyar jog alapj�n.

### Szellemi tulajdon

Az Alkalmaz�s �s valamennyi kapcsol�d� v�djegy, szerz�i jogi alkot�s �s egy�b - ak�r bejegyzett, ak�r be nem jegyzett - szellemi tulajdon
(a tov�bbiakban egy�ttesen: Szellemi Tulajdon) tulajdonosa az EKE �s/vagy EKE Szolg�ltat�, valamint az alkalmaz�shoz kedvezm�nyt ny�jt�
partnerek. A Felhaszn�l�k az Alkalmaz�st a Szellemi Tulajdon maxim�lis tiszteletben tart�s�val jogosultak haszn�lni. 

A Szellemi Tulajdon kiterjed k�l�n�sen, de nem kiz�r�lagosan valamennyi szoftverre, log�ra, m�rkajelre, m�rkan�vre, f�nyk�pre, sz�vegre, grafik�ra, adatb�zisra.
A Szellemi Tulajdonnak tilos b�rminem� megs�rt�se, bitorl�sa, m�sol�sa, �tdolgoz�sa �s tilos azt b�rmilyen egy�b m�don megs�rteni,
azt jogosulatlanul felhaszn�lni, tov�bbadni, megterhelni, azzal b�rmilyen m�don rendelkezni, vissza�lni. 

Ezen szab�lyok megs�rt�se az Alkalmaz�s haszn�lati lehet�s�geinek azonnali hat�ly� megsz�ntet�se mellett a megfelel� jogi l�p�sek megt�tel�t
� bele�rtve esetleges b�ntet�jogi l�p�sek megt�tel�t is � vonja maga ut�n a Felhaszn�l�val, m�s jogs�rt� szem�llyel szemben a Tulajdonos �s/vagy a 
Szellemi Tulajdon egy�b jogosultjai �ltal.


### Haszn�lat



### Felel�ss�gi szab�lyok

Az Alkalmaz�shoz kapcsol�d� adatb�zis m�dos�t�sa kiz�r�lag az �zemeltet� �ltal, illetve az Alkalmaz�st �zemeltet� webkiszolg�l�n kereszt�l
lehets�ges. B�rmilyen k�ls�, nem az Alkalmaz�s r�szek�nt el�rhet� eszk�zzel t�rt�n� beavatkoz�s a Felhaszn�l� azonnali kiz�r�s�t eredm�nyezi.

Ha a Felhaszn�l� az Alkalmaz�st haszn�lat k�zben bez�rja, vagy ha a kapcsolat (b�rmely okb�l) megszakad a kiszolg�l� webhely�vel,
abban az esetben az adatok elveszt�s��rt a Tulajdonos semmilyen felel�ss�get nem v�llal. A Tulajdonos �s az �zemeltet� a rendelkez�s�re �ll�
eszk�z�kkel biztos�tja, hogy az Alkalmaz�s haszn�lata technikai szempontb�l biztons�gosnak min�s�lj�n.

Az Alkalmaz�shoz val� csatlakoz�s miatt bek�vetkez� k�rok�rt, az internetes h�l�zat esetleges �zemkimarad�s�b�l, 
az el�r�si �t hib�j�b�l, b�rmely nem v�rt technikai hib�b�l ered� adatveszt�s�rt, v�rusb�l, vagy m�s k�rok�rt a Tulajdonos nem felel�s. 
A Felhaszn�l�knak minden esetben fel kell m�rni�k, hogy rendelkeznek-e az Alkalmaz�s haszn�lat�hoz sz�ks�ges ismeretekkel, 
technikai k�vetelm�nyekkel �s teljes�tm�nyekkel.
A Tulajdonos fenntartja mag�nak a jogot arra, hogy amennyiben valamely Felhaszn�l� r�sz�r�l b�rmilyen manipul�ci�t, t�megesen gener�lt let�lt�st,
illetve az Alkalmaz�s szellem�vel b�rmilyen m�don �sszef�rhetetlen vagy azt s�rt� magatart�st tapasztal, 
vagy ennek megalapozott gyan�ja felmer�l, �gy a Felhaszn�l�t azonnali hat�llyal kiz�rja az Alkalmaz�s felhaszn�l�i k�r�b�l.



### Technikai k�vetelm�nyek
Az Alkalmaz�s haszn�lat�hoz sz�ks�ges technikai felt�telek: Windows 10 oper�ci�s rendszer valamint minimum 400 MB szabad t�rhely. 
A technikai felt�teleket az Alkalmaz�s let�lt�s�hez �s haszn�lat�hoz a Felhaszn�l�nak kell teljes�tenie. A technikai felt�telek nem teljes�l�s��rt a Tulajdonos nem vonhat� felel�ss�gre.
Ugyan�gy nem vonhat� felel�ss�gre a Tulajdonos az Alkalmaz�s haszn�lat�b�l a k�sz�l�ken bek�vetkez� adatveszt�s�rt, meghib�sod�s�rt. 
A Tulajdonos kiz�r minden k�rt�r�t�si felel�ss�get az Alkalmaz�shoz csatlakoz� minden k�ls� szerver �ltal ny�jtott
vagy megjelen�tett adattal, inform�ci�val kapcsolatban is.

Az Alkalmaz�s telep�t�ssel vehet� haszn�latba.


### Garancia �s k�rt�r�t�s

Az Alkalmaz�s haszn�lat�hoz a felhaszn�l�i oldalon sz�ks�ges � fent meghat�rozott vagy b�rmely egy�b - technikai felt�teleket a Felhaszn�l�nak kell biztos�tania, teljes�tenie.
Ezen technikai felt�telek nem teljes�l�s��rt a Tulajdonos nem vonhat� felel�ss�gre. Ugyan�gy nem vonhat� felel�ss�gre a Tulajdonos az Alkalmaz�s haszn�lat�b�l ad�d�an, 
a k�sz�l�ken bek�vetkez� adatveszt�s�rt, meghib�sod�s�rt. A Tulajdonos kiz�r minden k�rt�r�t�si felel�ss�get az Alkalmaz�shoz csatlakoz� minden k�ls� szoftver �ltal ny�jtott
vagy megjelen�tett adattal, inform�ci�val kapcsolatban. A Tulajdonos nem v�llal garanci�t az Alkalmaz�s megszak�t�smentes m�k�d�s��rt, 
valamint vis major hib�k�rt. Az ebb�l ered� adatveszt�s�rt, tartalom veszt�s�rt a Tulajdonos szint�n nem tartozik k�rt�r�t�si felel�ss�ggel.


### Egy�b rendelkez�sek

Jelen Felhaszn�l�si Felt�telekben nem szab�lyozott k�rd�sekben a hat�lyos jogszab�lyok � k�l�n�sen,
de nem kiz�r�lagosan a Polg�ri T�rv�nyk�nyvr�l sz�l� 2013. �vi V. t�rv�ny, az Eur�pai Parlament �s Tan�cs 2016. �prilis 27-i (EU) 2016/679 Rendelete
a term�szetes szem�lyeknek a szem�lyes adatok kezel�se tekintet�ben t�rt�n� v�delm�r�l �s az ilyen adatok szabad �raml�s�r�l, valamint a 95/46/EK 
ir�nyelv hat�lyon k�v�l helyez�s�r�l, az inform�ci�s �nrendelkez�si jogr�l �s az inform�ci� szabads�gr�l sz�l� 2011. �vi CXII. t�rv�ny, a szerz�i jogr�l
sz�l� 1999. �vi LXXVI. t�rv�ny, valamint az elektronikus kereskedelmi szolg�ltat�sok, valamint az inform�ci�s t�rsadalommal �sszef�gg� szolg�ltat�sok
egyes k�rd�seir�l sz�l� 2001. �vi CVIII. t�rv�ny � rendelkez�sei az ir�nyad�ak.

### Kapcsolat

Az Alkalmaz�s hossz�t�v�, megfelel� m�k�d�s�hez a szoftver �zemeltet�s�t �s t�mogat�s�t a Fenntart� v�gzi munkanapokon, 8:00 �s 16:00 k�z�tt
Az Alkalmaz�s m�k�d�s�vel kapcsolatban a fejleszt�k k�z�sen ezen c�lra fenntartott e-mail c�m�re
(tov�bbiakban: *NTBSLHK@gmail.com*) v�rjuk a szolg�ltat�ssal kapcsolatosan felmer�l� k�rd�seit, tapasztalatait.
A Fenntart� igyekszik a fentebb eml�tett id�szakban a k�rd�seket kiel�g�t�en megv�laszolni.
A v�ltoztat�s joga �s lehet�s�ge fejleszt�s r�v�n abszol�t m�don fenn�ll.

### Jelenlegi �zleti folyamatok

Jelenlegi helyzet�nk, nevezetesen a j�rv�nyhelyzet valamint a kor�bbi oktat�si modellek hi�nyoss�gai
�jabb digitaliz�ci�s l�p�sekre sarkallj�k a fels�oktat�si szf�r�t is. Ezen inform�ci� �rtelm�ben sz�ks�geltetik
egy olyan webhely fel�p�t�se, amelyen kereszt�l biztos�tjuk a hallgat�k a gyakorlatokhoz elv�rt, 
megfelel� szint� �s nyelvezet� tananyaghoz, tov�bb� a gyakorlatban felmer�l� feladatokhoz val� hozz�f�r�s�t.
A megrendel� fontosnak tartja tov�bb�, hogy a di�kok visszajelz�seket kapjanak a feladatokhoz csatolt megold�saikhoz.

### Ig�nyelt �zleti folyamatok

Fent eml�tett okokb�l k�vetkez�en c�g�nknek is haladnia kell jelen korunk egyre n�vekv� elv�r�saival, 
�s ez�ltal sz�ks�ges l�p�ss� v�lt egy j�l funkcion�l� feladatkioszt� rendszer ki�p�t�se.
Ezalatt egy online webes fel�letet �rt�nk, amelynek seg�ts�g�vel lehet�s�get kapnak 
az int�zm�ny tan�rai egy szerveren t�rolt adatb�zisba kigy�jteni a hallgat�knak sz�nt feladatok r�szleteit.

### Fogalomt�r
	- Grafikus felhaszn�l�i fel�let - GUI: a sz�m�t�g�p �s ember k�zti kapcsolatot megval�s�t� elemek �sszess�ge. 
	- weboldal: gyakorlatilag az interneten tal�lhat�, hipertext dokumentum, amelyet valamilyen b�ng�sz�programmal lehet megjelen�teni. Tartalmaz k�l�nb�z� objektumokat: k�peket, sz�veget, t�bl�zatokat, hivatkoz�sokat m�s weboldalakra stb. 
	A webb�ng�sz� ezen adathalmazra fogalmaz meg egy �gynevezett HTTP-GET-k�r�st, ami azt eredm�nyezi, hogy a b�ng�sz� fel�let�n megjelenik a lek�rdezett weboldal a le�r�nyelv� dokumentum (html - css) alapj�n megfelel�en form�zva.
	- adatb�zis: azonos min�s�g�, megfelel�en struktur�lt diszkr�t adatok �sszess�ge, amelyet egy azok t�rol�s�ra, lek�rdez�s�re �s m�dos�t�s�ra k�l�nb�z� adatb�zis-kezel� szoftvereket haszn�lunk. 
	C�lja az adatok megb�zhat�, perzisztens t�rol�sa �s viszonylag/kell�en gyors lek�rdezhet�s�g�nek biztos�t�sa.