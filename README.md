### Projekta uzdevums: ###
Projektam izvēlēts aktuāls mājsaimniecības jautājums - dabasgāzes pakalpojumu sniedzēja izvēle. Jāapkopo ziņas par dabasgāzes patēriņu pēdējā gada laikā, jānoskaidro gāzes vidējais mēneša patēriņš gada griezumā. Dabasgāzes vidējais mēneša patēriņš jāievada gāzes pakalpojumu tīmekļa lapu mēneša maksas kalkulatoros, un katra pakalpojumu sniedzēja izdevīgākā tarifu summa jāsaglabā.
Informācija par dabasgāzes patēriņu gada laikā apkopota saņemtajos rēķinos PDF formātā. No tiem jāizdala dabasgāzes patēriņa apjoms kubikmetros attiecīgajā mēnesī. Tas atrodams sadaļā "SADALES SISTĒMAS OPERATORA AS “GASO” INFORMĀCIJA PAR DABASGĀZES PATĒRIŅU". Saskaitot šo apjomu un izdalot to ar mēnešu skaitu, iegūst vidējo mēneša dabasgāzes patēriņu kubikmetros, kuru noapaļo līdz veselam skaitlim.
Latvijā ar dabasgāzes tirdzniecību mājsaimniecībām nodarbojas uzņēmumi _Latvijas Gāze_, _Elektrum_ un _Elenger_. Šo uzņēmumu tīmekļa lapās pieejami kalkulatori, kas aprēķina eventuālo vidējo mēneša maksu par dabasgāzi, balstoties uz vidējo mēneša patēriņu. Tādēļ dabasgāzes vidējo mēneša patēriņa skaitli jāievada šajos kalkulatoros un jāizgūst dabasgāzes tirgotāja izdevīgākais piedāvājums, kas tiek piedāvāts kā pirmais uzskaitījumā. Iegūtie dati jāsaglabā _Excel_ datnē.

### Nepieciešamās _Python_ bibliotēkas: ###
Projekta izpildei nepieciešamas semestra nodarbību gaitā apskatītās bibliotēkas. 
1. __PyPDF2__ bibliotēka, kas ļauj strādāt ar PDF failiem un ļauj izgūt no tiem nepieciešamo informāciju.
2. __OS__ bibliotēka, kas ļauj strādāt ar operētājsistēmas struktūru - direktorijām un failiem.
3. __Selenium__ bibliotēka, ar kuras palīdzību tīmekļa lapās ievadīt un izgūt informāciju. 
4. __Time__ bibliotēka laika menedmentam, kas, strādājot ar tīmekļa lapām, nodrošina, ka lapa paspēj ielādēties.
4. __Openpyxl__ bibliotēka, lai izveidotu _Excel_ datni ar projekta izpildes rezultātiem.

### Piezīmes projekta izpildē: ###
1. PDF rēķinu failu noformējums nebija viendabīgs, bet mēģinājumu un kļūdu ceļā izdevās atrast kompaktu risinājumu, kas der visiem gadījumiem.
2. _Elektrum_ tīmekļa lapā summas skaitlis bija sadalīts trīs daļās: divās skaitļa daļās un atdalītājā (komatā) - tas gan ļāva vienkāršāk pievienot vajadzīgo atdalītāju.
3. _Latvijas Gāzes_ tīmekļa lapā neizdevās identificēt uznirstošā sākuma loga pogas, bet izrādījās, ka kalkulators darbojas arī tad, ja sākuma logs ir atvērts.
