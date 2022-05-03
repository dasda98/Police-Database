from PoliceDatabase import app
from PoliceDatabase import db

"""
                                                            DATABASE MODELS
"""

################################################################################################################################################
class Police_Station(db.Model):                                                                                                                 
                                                                                                                                                
    __tablename__ = 'komisariat'                                                                                                                
                                                                                                                                                
    id_komisariat = db.Column('id_komisariat', db.Integer, db.Sequence('komisariat_seq'), primary_key = True)                                   
    nazwa         = db.Column(db.String(30))                                                                                                    
    nr_telefonu   = db.Column(db.Integer)                                                                                                       
    miasto        = db.Column(db.String(30))                                                                                                    
    adres         = db.Column(db.String(30))                                                                                                    
                                                                                                                                                
    
    def __init__(self, nazwa, nr_telefonu, miasto, adres):                                                                                      
        self.nazwa         = nazwa                                                                                                              
        self.nr_telefonu   = nr_telefonu                                                                                                        
        self.miasto        = miasto                                                                                                             
        self.adres         = adres                                                                                                              
################################################################################################################################################
                                                                                                                                                
class Police_Car(db.Model):                                                                                                                     
                                                                                                                                                
    __tablename__ = 'radiowoz'                                                                                                                  
                                                                                                                                                
    id_radiowoz   = db.Column('id_radiowoz', db.Integer, db.Sequence('radiowoz_seq'), primary_key = True)                                       
    rejestracja   = db.Column(db.String(30))                                                                                                    
    numer         = db.Column(db.String(30))                                                                                                    
    id_komisariat = db.Column(db.Integer)                                                                                                       
                                                                                                                                                                                                               
                                                                                                                                                
    def __init__(self, rejestracja, numer, id_komisariat):                                                                                      
        self.rejestracja = rejestracja                                                                                                          
        self.numer = numer                                                                                                                      
        self.id_komisariat = id_komisariat                                                                                                      
################################################################################################################################################
                                                                                                                                                
class Patrol(db.Model):                                                                                                                         
                                                                                                                                                
    __tablename__ = 'patrol'                                                                                                                    
                                                                                                                                                
    id_patrol   = db.Column('id_patrol', db.Integer, db.Sequence('patrol_seq'), primary_key = True)                                             
    id_radiowoz = db.Column('id_radiowoz', db.Integer, db.ForeignKey('radiowoz.id_radiowoz'))                                                   
    miejsce     = db.Column(db.String(30))         
    
    radiowoz = db.relationship('Police_Car', foreign_keys=id_radiowoz)                                                                          
                                                                                                                                                
    def __init__(self, id_radiowoz, miejsce):                                                                                                   
        self.id_radiowoz = id_radiowoz                                                                                                          
        self.miejsce     = miejsce                                                                                                              
################################################################################################################################################
                                                                                                                                                
class Rank(db.Model):                                                                                                                           
                                                                                                                                                
    __tablename__ = 'ranga'                                                                                                                     
                                                                                                                                                
    id_ranga = db.Column('id_ranga', db.Integer, db.Sequence('ranga_seq'), primary_key = True)                                                  
    tytul    = db.Column(db.String(30))                                                                                                         
    pensja   = db.Column(db.String(30))                                                                                                         
                                                                                                                                                
    #policjanci = db.relationship('Police_Member', backref='ranga', lazy=True)                                                                  
                                                                                                                                                
    def __init__(self, tytul, pensja):                                                                                                          
        self.pensja   = pensja                                                                                                                  
        self.tytul    = tytul                                                                                                                   
################################################################################################################################################
                                                                                                                                                
class Police_Member(db.Model):                                                                                                                  
                                                                                                                                                
    __tablename__ = 'policjant'                                                                                                                 
                                                                                                                                                
    id_policja    = db.Column('id_policja', db.Integer, db.Sequence('policjant_seq'), primary_key = True)                                       
    nr_telefonu   = db.Column(db.Integer)                                                                                                       
    miasto        = db.Column(db.String(30))                                                                                                    
    adres         = db.Column(db.String(30))                                                                                                    
    imie		  = db.Column(db.String(30))                                                                                                    
    nazwisko      = db.Column(db.String(30))                                                                                                    
    id_radiowoz	  = db.Column('id_radiowoz', db.Integer, db.ForeignKey("radiowoz.id_radiowoz"))                                                 
    id_ranga 	  = db.Column('id_ranga', db.Integer, db.ForeignKey("ranga.id_ranga"))                                                          
    id_komisariat = db.Column('id_komisariat', db.Integer, db.ForeignKey("komisariat.id_komisariat"))                                           
                                                                                                                                                
    radiowoz = db.relationship('Police_Car', foreign_keys=id_radiowoz)                                                                                                                                        
    ranga = db.relationship('Rank', foreign_keys=id_ranga)                                                                                                                                        
    komisariat = db.relationship('Police_Station', foreign_keys=id_komisariat)  
                                                                                                                                                
    def __init__(self ,nr_telefonu, miasto, adres, imie, nazwisko, id_radiowoz, id_ranga, id_komisariat):                                       
        self.nr_telefonu   = nr_telefonu                                                                                                        
        self.miasto        = miasto                                                                                                             
        self.adres         = adres                                                                                                              
        self.imie		   = imie		                                                                                                        
        self.nazwisko      = nazwisko                                                                                                           
        self.id_radiowoz   = id_radiowoz	                                                                                                    
        self.id_ranga 	   = id_ranga 	                                                                                                        
        self.id_komisariat = id_komisariat                                                                                                      
################################################################################################################################################
                                                                                                                                                
class Criminal_Member(db.Model):                                                                                                                
                                                                                                                                                
    __tablename__ = 'przestepca'                                                                                                                
                                                                                                                                                
    id_przestepcy = db.Column('id_przestepcy', db.Integer, db.Sequence('przestepca_seq'), primary_key = True)                                   
    imie          = db.Column(db.String(30))                                                                                                    
    nazwisko      = db.Column(db.String(30))                                                                                                    
    nr_telefonu   = db.Column(db.Integer)                                                                                                       
    miasto        = db.Column(db.String(30))                                                                                                    
    adres         = db.Column(db.String(30))                                                                                                    
                                                                                                                                                
    #przestepstwo = db.relationship('Crime', backref='przestepca', lazy=True)                                                                   
                                                                                                                                                
    def __init__(self, imie, nazwisko, nr_telefonu, miasto, adres):                                                                                                                                                                                 
        self.imie          = imie                                                                                                               
        self.nazwisko      = nazwisko                                                                                                           
        self.nr_telefonu   = nr_telefonu                                                                                                        
        self.miasto        = miasto                                                                                                             
        self.adres         = adres                                                                                                              
################################################################################################################################################
                                                                                                                                                
class Type_of_criminal(db.Model):                                                                                                               
                                                                                                                                                
    __tablename__ = 'rodzja_przestepstwa'                                                                                                       
                                                                                                                                                
    id_rodzja_przestepstwa   = db.Column('id_rodzja_przestepstwa', db.Integer, db.Sequence('rodzja_przestepstwa_seq'), primary_key = True)      
    nazwa_popelnionego_czynu = db.Column(db.String(30))                                                                                         
    oplata                   = db.Column(db.Integer)                                                                                            
                                                                                                                                                
    #przestepca = db.relationship('Crime', backref='rodzja_przestepstwa', lazy=True)                                                            
                                                                                                                                                
    def __init__(self, id_rodzja_przestepstwa, nazwa_popelnionego_czynu, oplata):                                                                                                                                               
        self.nazwa_popelnionego_czynu = nazwa_popelnionego_czynu                                                                                
        self.oplata                   = oplata                                                                                                  
#################################################################################################################################################
                                                                                                                                                
class Crime(db.Model):                                                                                                                          
                                                                                                                                                
    __tablename__ = 'przestepstwo'                                                                                                              
                                                                                                                                                
    id_przestepstwa        = db.Column('id_przestepstwa', db.Integer, db.Sequence('przestepstwo_seq'), primary_key = True)                      
    id_przestepcy          = db.Column('id_przestepcy', db.Integer, db.ForeignKey("przestepca.id_przestepcy"))                                  
    id_policjant           = db.Column('id_policjant', db.Integer, db.ForeignKey('policjant.id_policja'))
    id_rodzja_przestepstwa = db.Column('id_rodzja_przestepstwa', db.Integer, db.ForeignKey("rodzja_przestepstwa.id_rodzja_przestepstwa"))       
    data_przestepstwa      = db.Column(db.String(30))

    przestepca = db.relationship('Criminal_Member', foreign_keys=id_przestepcy)                                                                                                                                        
    policjant = db.relationship('Police_Member', foreign_keys=id_policjant)                                                                                                                                        
    rodzaj_przestepstwa = db.relationship('Type_of_criminal', foreign_keys=id_rodzja_przestepstwa)
                                                                                                                                                
    #przestepstwo = db.relationship('Police_Criminal', backref='przestepstwo', lazy=True)                                                       
                                                                                                                                                
    def __init__(self, id_przestepcy, id_policjant, id_rodzja_przestepstwa, data_przestepstwa):                                                                                                                                           #
        self.id_przestepcy          = id_przestepcy  
        self.id_policjant           = id_policjant                                                                                              
        self.id_rodzja_przestepstwa = id_rodzja_przestepstwa                                                                                    
        self.data_przestepstwa      = data_przestepstwa                                                                                         
#################################################################################################################################################
                                                                                                                                                
#class Police_Criminal(db.Model):                                                                                                                
#                                                                                                                                                
#    __tablename__ = 'policjant_przestepstwo'                                                                                                    
#                                                                                                                                                
#    id_policjant    = db.Column('id_policjant', db.Integer, db.ForeignKey("policjant.id_policja", primary_key=True))                            
#    id_przestepstwo = db.Column('id_przestepstwo', db.Integer, db.ForeignKey("przestepstwo.id_przestepstwa"), primary_key=True)   
#
#    #przestepstwo = db.relationship('Criminal_Member', foreign_keys=id_przestepstwo)                                                                                                                                        
#    #policjant = db.relationship('Police_Member', foreign_keys=id_przestepstwo)
#                                                                                                                                                
#    def __init__(self, id_policjant, id_przestepstwo):                                                                                          
#        self.id_policjant    = id_policjant                                                                                                     
#        self.id_przestepstwo = id_przestepstwo                                                                                                  
##################################################################################################################################################
