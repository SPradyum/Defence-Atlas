# data_store.py

BASE_PATH = r"E:\Documents\Projects\Python\Defence Atlas\assets"

DASHBOARD_BG = rf"{BASE_PATH}\images\Indian Defence.png"

DEFENCE_DATA = {

    "Army": {
        "theme_color": "#556B2F",

        "about":
            "The Indian Army is the land-based branch of the Indian Armed Forces and "
            "is one of the largest standing armies in the world. Its primary mission "
            "is to ensure national security and unity, defend the nation from external "
            "aggression, and maintain peace within its borders. The Army also plays a "
            "vital role in disaster relief, humanitarian assistance, and peacekeeping operations.",

        "motto":
            "Service Before Self (Seva Paramo Dharma)",

        "commands":
            "The Indian Army operates through seven commands. Six are operational commands "
            "— Northern, Western, Eastern, Southern, Central, and South Western — each "
            "responsible for specific geographic regions. The Training Command (ARTRAC) "
            "oversees doctrine development and training standards.",

        "ranks":
            "The rank structure of the Indian Army begins with commissioned officers such as "
            "Lieutenant, Captain, and Major, progressing to senior leadership ranks including "
            "Colonel, Brigadier, Major General, Lieutenant General, and General.",

        "equipment":
            "The Indian Army operates a wide range of modern equipment including T-90 Bhishma "
            "and Arjun main battle tanks, Pinaka multi-barrel rocket launchers, BrahMos cruise "
            "missiles, AK-203 assault rifles, and advanced artillery systems.",

        "established": "1 April 1895",
        "headquarters": "New Delhi",

        "bg_image": rf"{BASE_PATH}\background\army_bg.jpg",
        "logo": rf"{BASE_PATH}\images\army_logo.png"
    },

    "Air Force": {
        "theme_color": "#1E90FF",

        "about":
            "The Indian Air Force (IAF) is responsible for securing Indian airspace and "
            "conducting aerial warfare. It provides rapid mobility, surveillance, and "
            "precision strike capability, playing a decisive role in modern warfare and "
            "humanitarian operations.",

        "motto":
            "Touch the Sky with Glory (Nabhah Sparsham Deeptam)",

        "commands":
            "The IAF functions through operational and functional commands including Western, "
            "Eastern, Central, Southern, South Western, Training, and Maintenance Commands.",

        "ranks":
            "The officer ranks of the Indian Air Force include Flying Officer, Squadron Leader, "
            "Wing Commander, Group Captain, Air Commodore, Air Vice Marshal, Air Marshal, "
            "and Air Chief Marshal.",

        "equipment":
            "The IAF operates advanced aircraft such as Rafale, Su-30MKI, Tejas, Mirage-2000, "
            "Apache attack helicopters, Chinook heavy-lift helicopters, and C-17 Globemaster transport aircraft.",

        "established": "8 October 1932",
        "headquarters": "New Delhi",

        "bg_image": rf"{BASE_PATH}\background\airforce_bg.jpg",
        "logo": rf"{BASE_PATH}\images\airforce_logo.png"
    },

    "Navy": {
        "theme_color": "#0B3C5D",

        "about":
            "The Indian Navy safeguards India’s maritime borders and strategic interests. "
            "It ensures freedom of navigation in the Indian Ocean Region and conducts "
            "anti-piracy, surveillance, and humanitarian assistance missions.",

        "motto":
            "May the Lord of the Waters be Auspicious Unto Us (Sam No Varunah)",

        "commands":
            "The Navy operates under three commands — Western, Eastern, and Southern — "
            "with additional specialized units responsible for training, logistics, "
            "and strategic submarine operations.",

        "ranks":
            "Naval ranks range from Sub Lieutenant to Captain, Commodore, Rear Admiral, "
            "Vice Admiral, and Admiral, reflecting command responsibilities at sea.",

        "equipment":
            "Major naval assets include aircraft carriers INS Vikrant and INS Vikramaditya, "
            "destroyers, frigates, Kalvari-class submarines, and P-8I maritime patrol aircraft.",

        "established": "26 January 1950",
        "headquarters": "New Delhi",

        "bg_image": rf"{BASE_PATH}\background\navy_bg.webp",
        "logo": rf"{BASE_PATH}\images\navy_logo.png"
    },

    "NCC": {
        "theme_color": "#800000",

        "about":
            "The National Cadet Corps (NCC) is a youth development organization aimed at "
            "instilling discipline, leadership, patriotism, and social responsibility "
            "among students. It prepares young citizens for national service.",

        "motto":
            "Unity and Discipline (Ekta aur Anushasan)",

        "commands":
            "NCC functions through 17 Directorates across India, coordinating training "
            "activities, camps, and national integration programs.",

        "ranks":
            "Cadet ranks include Cadet, Lance Corporal, Corporal, Sergeant, Under Officer, "
            "and Senior Under Officer, reflecting leadership roles during training.",

        "equipment":
            "Training equipment includes drill rifles, map-reading tools, field craft kits, "
            "and survival training aids.",

        "established": "15 July 1948",
        "headquarters": "New Delhi",

        "bg_image": rf"{BASE_PATH}\background\ncc_bg.jpg",
        "logo": rf"{BASE_PATH}\images\ncc_logo.png"
    }
}
