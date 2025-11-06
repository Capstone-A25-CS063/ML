import random

def get_current_economic_indicators():
    """
    Mensimulasikan pengambilan data indikator ekonomi makro terkini.
    Di production, ganti ini dengan query database atau API call real.
    """
    # Simulasi nilai yang sedikit berfluktuasi di sekitar rata-rata dataset
    return {
        "emp.var.rate": round(random.uniform(-3.4, 1.4), 1),
        "cons.price.idx": round(random.uniform(92.2, 94.8), 3),
        "cons.conf.idx": round(random.uniform(-50.8, -26.9), 1),
        "euribor3m": round(random.uniform(0.6, 5.0), 3),
        "nr.employed": round(random.uniform(4963.6, 5228.1), 1)
    }