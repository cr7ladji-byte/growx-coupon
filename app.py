import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="GrowX Coupon API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/generate-coupon")
def generate_coupon():
    matches = [
        {"home": "Real Madrid", "away": "Valencia", "league": "La Liga"},
        {"home": "Arsenal", "away": "Brighton", "league": "Premier League"},
        {"home": "Bayern Munich", "away": "Frankfurt", "league": "Bundesliga"},
        {"home": "Inter Milan", "away": "Lazio", "league": "Serie A"},
        {"home": "PSG", "away": "Rennes", "league": "Ligue 1"},
        {"home": "Dortmund", "away": "Stuttgart", "league": "Bundesliga"},
        {"home": "Manchester City", "away": "Newcastle", "league": "Premier League"}
    ]
    
    markets = [
        "Plus de 1.5 buts", 
        "Remboursé si nul (DNB)", 
        "Les 2 équipes marquent", 
        "Plus de 8.5 corners", 
        "Double Chance (1X/X2)"
    ]
    random.shuffle(markets)

    selected = random.sample(matches, 5)
    selections = []
    total_odds = 1.0

    for idx, fix in enumerate(selected):
        odds = round(random.uniform(1.48, 1.68), 2)
        total_odds *= odds
        selections.append({
            "match": f"{fix['home']} vs {fix['away']}",
            "league": fix['league'],
            "market": markets[idx],
            "odds": odds
        })

    return {
        "brand": "GrowX Coupon",
        "total_odds": round(total_odds, 2),
        "combined_prob": round((1 / total_odds) * 100, 1),
        "selections": selections
    }

