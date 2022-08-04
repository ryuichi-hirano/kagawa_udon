from crypt import methods
from flask import Flask, render_template
import folium
import pandas as pd
from flask import Flask, Response, request, render_template
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
import os
import csv
import pathlib
import imghdr
from PIL import Image
import util
from dataaccess import DataAccess
from geopy.distance import geodesic
import numpy as np

app = Flask(__name__)

# print(DataAccess.get_latlng_by_sightseeing_name('屋島')[0])
print(DataAccess.get_latlng_by_udon_name('がもううどん')[0])

# spot_l = DataAccess.get_spot_name()
# spot_l = [s[0] for s in spot_l]
# udon_shop = DataAccess.get_udon_name()
# udon_shop = [u[0] for u in udon_shop]

@app.route('/')
def index():
    sightseeing = DataAccess.get_sightseeing()
    udon = DataAccess.get_udon()
    map_s = folium.Map(location=[34.2226, 134.0199], zoom_start=9)
    map_u = folium.Map(location=[34.2226, 134.0199], zoom_start=9)

    for s in sightseeing:
        folium.Marker(
            location=[s[2], s[3]],
            popup=s[1],
        ).add_to(map_s)

    for u in udon:
        folium.Marker(
            location=[u[2], u[3]],
            popup=u[1],
            icon=folium.Icon(color='red')
        ).add_to(map_u)
    return render_template('index.html', map_s=map_s._repr_html_(), map_u=map_u._repr_html_()) 

@app.route('/udon_nearby', methods=['GET', 'POST'])
def udon_nearby():
    spot_l = DataAccess.get_spot_name()
    spot_l = [s[0] for s in spot_l]
    udon_l = DataAccess.get_all_latlng_udon()

    map_s = folium.Map(location=[34.2226, 134.0199], zoom_start=9)

    if request.method == "POST":
        spot = request.form.get("sightseeing_spot")
        spo_ll = DataAccess.get_latlng_by_sightseeing_name(spot)[0]
        folium.Marker(
            location=[spo_ll[0], spo_ll[1]], 
            popup=spot
        ).add_to(map_s)

        disses = []
        for u in udon_l:
            dis = geodesic(spo_ll, u[1:])
            disses.append(dis)

        max_index = np.argmin(disses)
        folium.Marker(
            location=[udon_l[max_index][1], udon_l[max_index][2]], 
            icon=folium.Icon(color='red'),
            popup=udon_l[max_index][0]
        ).add_to(map_s)
    else:
        spot = 'dummy'


    return render_template('udon_nearby.html', map_s=map_s._repr_html_(), spot_l = spot_l, spot=spot) 

@app.route('/spot_nearby', methods=['GET', 'POST'])
def spot_nearby():
    udon_shop = DataAccess.get_udon_name()
    udon_shop = [u[0] for u in udon_shop]
    spot_l = DataAccess.get_all_latlng_spot()

    map_s = folium.Map(location=[34.2226, 134.0199], zoom_start=9)
    map_u = folium.Map(location=[34.2226, 134.0199], zoom_start=9)

    if request.method == "POST":
        udon = request.form.get("udon_shop_")
        udon_ll = DataAccess.get_latlng_by_udon_name(udon)[0]
        # print(udon_ll[0])

        folium.Marker(
            location=[udon_ll[0], udon_ll[1]], 
            popup=udon
        ).add_to(map_u)

        disses = []
        for u in spot_l:
            dis = geodesic(udon_ll, u[1:])
            disses.append(dis)

        max_index = np.argmin(disses)
        folium.Marker(
            location=[spot_l[max_index][1], spot_l[max_index][2]], 
            icon=folium.Icon(color='red'),
            popup=spot_l[max_index][0]
        ).add_to(map_u)

    else:
        udon = 'dummy'


    return render_template('spot_nearby.html',map_u=map_u._repr_html_(), udon=udon, udon_shop=udon_shop) 


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)