# nameMangle.py
  Created by: Nick Sanzotta/@beamr
  Description: Mangles usernames into common naming conventions 
  Script Version: nameMangle v1.0

	Usage: ./nameMangle.py <OPTIONS> 
	Ex: ./nameMangle.py -m 7 -d yahoo.com -i /names.txt
	Mangled output saved to: nameMangle/nameMangle-data/format[x]_time.txt 

#Mangle options:

	 -m <mangle>		  
                                 1)FirstLast        ex:nicksanzotta
                                 2)LastFirst        ex:sanzottanick
                                 3)First.Last       ex:nick.sanzotta
                                 4)Last.First       ex:sanzotta.nick
                                 5)First_Last       ex:nick_sanzotta
                                 6)Last_First       ex:sanzotta_nick
                                 7)FLast            ex:nsanzotta
                                 8)LFirst           ex:snick
                                 9)FirstL           ex:nicks
                                10)F.Last           ex:n.sanzotta
                                11)L.Firstname      ex:s.nick
                                12)FirLa            ex:nicsa
                                13)Lastfir          ex:sanznic  
    
	 -d <domain>		Append @domain.com to user list.
	 -i <input>		Input file (Format must be ex: ).
