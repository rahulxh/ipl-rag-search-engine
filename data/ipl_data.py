"""
IPL Knowledge Base - Sample data chunks for RAG ingestion.
In production, replace/extend this with real scraped or CSV data.
"""

IPL_DOCUMENTS = [
    # Teams
    {
        "id": "team_csk",
        "text": "Chennai Super Kings (CSK) is one of the most successful IPL franchises. They are captained by MS Dhoni and are based in Chennai. Their home ground is M. A. Chidambaram Stadium. CSK has won the IPL title multiple times and is known for their consistent performances. Key players include MS Dhoni, Ravindra Jadeja, and Ruturaj Gaikwad.",
        "metadata": {"category": "team", "team": "CSK"}
    },
    {
        "id": "team_mi",
        "text": "Mumbai Indians (MI) is the most successful IPL team with 5 IPL titles. They are owned by Reliance Industries and captained by Hardik Pandya. Their home ground is Wankhede Stadium. Key players include Rohit Sharma, Jasprit Bumrah, and Suryakumar Yadav. Mumbai Indians won titles in 2013, 2015, 2017, 2019, and 2020.",
        "metadata": {"category": "team", "team": "MI"}
    },
    {
        "id": "team_rcb",
        "text": "Royal Challengers Bengaluru (RCB) is based in Bengaluru. They are known for their passionate fanbase and have reached the finals multiple times but are yet to win the IPL title. Virat Kohli has been the face of RCB for many years. Their home ground is M. Chinnaswamy Stadium. RCB is known for producing high-scoring matches.",
        "metadata": {"category": "team", "team": "RCB"}
    },
    {
        "id": "team_kkr",
        "text": "Kolkata Knight Riders (KKR) is owned by Shah Rukh Khan and is based in Kolkata. They have won the IPL title twice, in 2012 and 2014. Their home ground is Eden Gardens. KKR won the IPL 2024 title under Shreyas Iyer's captaincy. Key players include Sunil Narine, Andre Russell, and Venkatesh Iyer.",
        "metadata": {"category": "team", "team": "KKR"}
    },
    {
        "id": "team_srh",
        "text": "Sunrisers Hyderabad (SRH) is based in Hyderabad. They won the IPL title in 2016 under David Warner's captaincy. Their home ground is Rajiv Gandhi International Cricket Stadium. SRH is known for their strong bowling attack. Key players include Pat Cummins, Heinrich Klaasen, and Travis Head.",
        "metadata": {"category": "team", "team": "SRH"}
    },
    {
        "id": "team_dc",
        "text": "Delhi Capitals (DC), formerly Delhi Daredevils, is based in Delhi. They have never won the IPL title but reached the finals in 2020. Their home ground is Arun Jaitley Stadium. Key players include Rishabh Pant, Axar Patel, and David Warner.",
        "metadata": {"category": "team", "team": "DC"}
    },
    {
        "id": "team_pbks",
        "text": "Punjab Kings (PBKS), formerly Kings XI Punjab, is based in Mohali. They have never won the IPL title. Their home ground is Punjab Cricket Association IS Bindra Stadium. Key players include Shikhar Dhawan and Liam Livingstone.",
        "metadata": {"category": "team", "team": "PBKS"}
    },
    {
        "id": "team_rr",
        "text": "Rajasthan Royals (RR) won the inaugural IPL title in 2008 under Shane Warne's captaincy. They are based in Jaipur and their home ground is Sawai Mansingh Stadium. RR won their second IPL title in 2022 under Sanju Samson. Key players include Sanju Samson, Jos Buttler, and Yuzvendra Chahal.",
        "metadata": {"category": "team", "team": "RR"}
    },
    {
        "id": "team_lsg",
        "text": "Lucknow Super Giants (LSG) is one of the newer IPL franchises, introduced in 2022. They are based in Lucknow and play at Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium. They have qualified for the playoffs in their debut seasons. Key players include KL Rahul and Nicholas Pooran.",
        "metadata": {"category": "team", "team": "LSG"}
    },
    {
        "id": "team_gt",
        "text": "Gujarat Titans (GT) is another newer franchise introduced in 2022. They won the IPL title in their very first season in 2022, and again in 2023, making them back-to-back champions. They are captained by Shubman Gill. Key players include Shubman Gill, Mohammed Shami, and Rashid Khan.",
        "metadata": {"category": "team", "team": "GT"}
    },

    # Players
    {
        "id": "player_kohli",
        "text": "Virat Kohli is the all-time leading run scorer in IPL history with over 7000 runs. He plays for Royal Challengers Bengaluru (RCB). Kohli is known for his consistency and has won the Orange Cap multiple times. He scored 973 runs in IPL 2016, which is the highest runs in a single IPL season. Kohli is a right-handed batsman.",
        "metadata": {"category": "player", "player": "Virat Kohli", "team": "RCB"}
    },
    {
        "id": "player_dhoni",
        "text": "MS Dhoni is widely regarded as the greatest IPL captain. He has led Chennai Super Kings (CSK) to multiple IPL titles. Dhoni is famous for his finishing abilities and calm demeanor under pressure. He is known as 'Captain Cool'. Dhoni has won IPL titles in 2010, 2011, 2018, 2021, and 2023 with CSK.",
        "metadata": {"category": "player", "player": "MS Dhoni", "team": "CSK"}
    },
    {
        "id": "player_rohit",
        "text": "Rohit Sharma is the most successful IPL captain, having led Mumbai Indians to 5 IPL titles. He is a right-handed opening batsman known for his elegant strokeplay. Rohit has scored over 6000 IPL runs. He is known for his ability to play big innings and anchor the innings.",
        "metadata": {"category": "player", "player": "Rohit Sharma", "team": "MI"}
    },
    {
        "id": "player_bumrah",
        "text": "Jasprit Bumrah plays for Mumbai Indians and is considered one of the best fast bowlers in T20 cricket. He has a unique bowling action and is deadly in the death overs. Bumrah has taken over 150 wickets in IPL. He was named the Purple Cap winner multiple times.",
        "metadata": {"category": "player", "player": "Jasprit Bumrah", "team": "MI"}
    },
    {
        "id": "player_warner",
        "text": "David Warner is an Australian left-handed opening batsman who has played for Sunrisers Hyderabad and Delhi Capitals in IPL. He has won the Orange Cap (most runs in a season) three times — in 2015, 2017, and 2019. Warner has scored over 6000 IPL runs and led SRH to the 2016 IPL title.",
        "metadata": {"category": "player", "player": "David Warner", "team": "SRH"}
    },
    {
        "id": "player_russell",
        "text": "Andre Russell is a West Indian all-rounder playing for Kolkata Knight Riders. He is famous for his explosive batting, often turning matches single-handedly with his hitting. Russell can hit sixes at will and is one of the most feared batsmen in T20 cricket. He also bowls medium-fast and has taken many wickets.",
        "metadata": {"category": "player", "player": "Andre Russell", "team": "KKR"}
    },
    {
        "id": "player_rashid",
        "text": "Rashid Khan is an Afghan leg-spin bowler who plays for Gujarat Titans. He is considered one of the best T20 bowlers in the world. Rashid is known for his googly and variations. He has taken over 150 IPL wickets and has an exceptional economy rate. He previously played for Sunrisers Hyderabad.",
        "metadata": {"category": "player", "player": "Rashid Khan", "team": "GT"}
    },

    # Records & Stats
    {
        "id": "record_orange_cap",
        "text": "The Orange Cap in IPL is awarded to the highest run scorer of the season. Virat Kohli holds the record for most runs in a single season with 973 runs in IPL 2016. Other notable Orange Cap winners include David Warner (3 times), Kane Williamson, and Jos Buttler who scored 863 runs in IPL 2022.",
        "metadata": {"category": "records", "type": "batting"}
    },
    {
        "id": "record_purple_cap",
        "text": "The Purple Cap in IPL is awarded to the highest wicket-taker of the season. Dwayne Bravo has won the Purple Cap the most times. Harshal Patel won it in 2021 with 32 wickets. Bhuvneshwar Kumar, Lasith Malinga, and Kagiso Rabada are other notable Purple Cap winners.",
        "metadata": {"category": "records", "type": "bowling"}
    },
    {
        "id": "record_highest_score",
        "text": "The highest team total in IPL history is 287/2 scored by Royal Challengers Bengaluru (RCB) against Pune Warriors India in 2013. Chris Gayle scored 175* off 66 balls in that match, which is also the highest individual score in IPL history. RCB vs PWI was played at M. Chinnaswamy Stadium, Bengaluru.",
        "metadata": {"category": "records", "type": "team_batting"}
    },
    {
        "id": "record_gayle",
        "text": "Chris Gayle is the only player to score a double century in ODI cricket, but in IPL his 175* off 66 balls against Pune Warriors in 2013 is the highest individual score. Gayle has scored the most centuries in IPL history with 6 hundreds. He played for multiple teams including RCB, KXIP, and MI.",
        "metadata": {"category": "player", "player": "Chris Gayle"}
    },

    # Seasons & Champions
    {
        "id": "ipl_champions",
        "text": "IPL Champions by year: 2008 - Rajasthan Royals, 2009 - Deccan Chargers, 2010 - Chennai Super Kings, 2011 - Chennai Super Kings, 2012 - Kolkata Knight Riders, 2013 - Mumbai Indians, 2014 - Kolkata Knight Riders, 2015 - Mumbai Indians, 2016 - Sunrisers Hyderabad, 2017 - Mumbai Indians, 2018 - Chennai Super Kings, 2019 - Mumbai Indians, 2020 - Mumbai Indians, 2021 - Chennai Super Kings, 2022 - Rajasthan Royals, 2023 - Chennai Super Kings, 2024 - Kolkata Knight Riders.",
        "metadata": {"category": "history", "type": "champions"}
    },
    {
        "id": "ipl_overview",
        "text": "The Indian Premier League (IPL) is a professional Twenty20 cricket league in India. It was founded by the Board of Control for Cricket in India (BCCI) in 2007. The first season was played in 2008. The league features 10 teams representing different Indian cities. IPL is one of the most attended cricket leagues globally and one of the richest sports leagues in the world. Each team plays 14 matches in the league stage, followed by playoffs.",
        "metadata": {"category": "general", "type": "overview"}
    },
    {
        "id": "ipl_format",
        "text": "IPL follows a double round-robin format in the league stage where each team plays every other team twice - once home and once away. The top 4 teams qualify for the playoffs. The playoffs consist of Qualifier 1 (1st vs 2nd), Eliminator (3rd vs 4th), Qualifier 2, and the Final. The team winning Qualifier 1 directly advances to the Final, while the other has a second chance through Qualifier 2.",
        "metadata": {"category": "general", "type": "format"}
    },
    {
        "id": "ipl_auction",
        "text": "IPL teams acquire players through auctions held every year. There is a player retention system where teams can retain a limited number of players before the auction. The mega auction is held every few years where teams release most players and rebuild their squads. Teams have a salary cap/purse limit they must stay within during auctions. The IPL auction is a high-profile event watched by cricket fans worldwide.",
        "metadata": {"category": "general", "type": "auction"}
    },
]
