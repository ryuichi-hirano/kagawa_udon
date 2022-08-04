from var import Var
from db import DB 

class DataAccess:

    def get_sightseeing():
        query = "SELECT * FROM kagawa_sightseeing"
        data = ()
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_udon():
        query = "SELECT * FROM kagawa_udon"
        data = ()
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_spot_name():
        query = "SELECT spot_name FROM kagawa_sightseeing"
        data = ()
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_udon_name():
        query = "SELECT spot_name FROM kagawa_udon"
        data = ()
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_latlng_by_sightseeing_name(spot_name):
        query = "SELECT spot_latitude, spot_longitude FROM kagawa_sightseeing WHERE spot_name = %s "
        data = (str(spot_name), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_latlng_by_udon_name(spot_name):
        query = "SELECT spot_latitude, spot_longitude FROM kagawa_udon WHERE spot_name = %s "
        data = (str(spot_name), )
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_all_latlng_spot():
        query = "SELECT spot_name, spot_latitude, spot_longitude FROM kagawa_sightseeing"
        data = ()
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    def get_all_latlng_udon():
        query = "SELECT spot_name, spot_latitude, spot_longitude FROM kagawa_udon"
        data = ()
        db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
        return db.execute(query, data)

    # def get_openclose_by_spot_name(self, spot_name):
    #     query = "SELECT spot_opentime, spot_closetime FROM data_spot WHERE spot_name = %s "
    #     data = (str(spot_name), )
    #     db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
    #     return db.execute(query, data)

    # def get_spot_by_features(self, feat1, feat2, feat3, feat4, feat5):
    #     query = "SELECT * FROM data_spot WHERE spot_history_culture = %s AND spot_food_product = %s AND spot_nature = %s AND spot_view = %s AND spot_experience = %s "
    #     data = (str(feat1), str(feat2), str(feat3), str(feat4), str(feat5), )
    #     db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
    #     return db.execute(query, data)

    # def get_spot_by_branch(self, branch):
    #     query = "SELECT * FROM data_spot WHERE spot_opentime < %s AND spot_closetime > %s "
    #     data = (str(branch), str(branch), )
    #     db = DB(Var.hostname, Var.port, Var.dbname, Var.username, Var.password)
    #     return db.execute(query, data)