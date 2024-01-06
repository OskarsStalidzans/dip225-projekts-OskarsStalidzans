### Projekta uzdevums: ###
Projektam izvēlēts aktuāls mājsaimniecības jautājums - gāzes pakalpojumu sniedzēja izvēle. Jāapkopo ziņas par gāzes patēriņu pēdējā gada laikā, jānoskaidro gāzes vidējais mēneša patēriņš gada griezumā. Gāzes vidējais mēneša patēriņš jāievada gāzes pakalpojumu tīmekļa lapu mēneša maksas kalkulatoros, un katra pakalpojuu sniedzēja izdevīgākā tarifu summa jāsaglabā.

### Nepieciešamās _ _Python_ _ bibliotēkas: ###
Projekta izpildei nepieciešamas semestra nodarbību gaitā apskatītās bibliotēkas. 
1. __PyPDF2__ bibliotēka, kas ļauj strādāt ar PDF failiem un ļauj izgūt no tiem nepieciešamo informāciju.
2. __OS__ bibliotēka, kas ļauj strādāt ar operētājsistēmas struktūru - irektorijām un failiem.
3. __Selenium__ bibliotēka, ar kuras palīdzību tīmekļa lapās ievadīt un izgūt informāciju. 
4. __Time__ bibliotēka laika menedmentam, kas, strādājot ar tīmekļa lapām, nodrošina, ka lapa paspēj ielādēties.
4. __Openpyxl__ bibliotēka, lai izveidotu _ _Excel_ _ datni ar projekta izpildes rezultātiem.

### Projekta izpildes gaita: ###
1. No rēķinu PDF failiem jāizgūst katra mēneša gāzes patēriņš kubikmetros.
2. Jāaprēķina gāzes vidējais mēneša patēriņš gada griezumā, noapaļojot līdz veselam skaitlim.
3. Jāievada gāzes vidējais mēneša patēriņš ikmēneša maksas kalkulatoros _ _Latvijas Gāzes_ _, _ _Elektrum_ _ un _ _Elenger_ _ tīmekļa lapās.
4. Izgūt no tīmekļa lapām iegūtos rezultātus - izdevīgākā tarifa plāna nosaukumu un ikmēneša maksu.
5. Saglabāt iegūtos datus _ _Excel_ _ datnē.

### Pārsteigumi projekta izpildē: ###
1. PDF rēķinu failu noformējums nebija viendabīgs, bet mēģinājumu un kļūdu ceļā izdevās atrast kompaktu risinājumu.
2. _ _Elektrum_ _ tīmekļa lapā summas skaitlis bija sadalīts trīs daļās: divās skaitļa daļās un atdalītājā (komatā) - tas gan ļāva vienkāršāk pievienot vajadzīgo atdalītāju.
3. _ _Latvijas Gāzes_ _ tīmekļa lapā neizdevās identificēt uznirstošā sākuma loga pogas, bet izrādījās, ka kalkulators darbojas arī tad, ja sākuma logs ir atvērts.