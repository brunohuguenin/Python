# Em Python, as chaves de um dicionário devem ser hashable (imutáveis).

locais = {
    (40.7128, -74.0060): "Nova York",
    (48.8566, 2.3522): "Paris"
}

for (lat, lon), cidade in locais.items():
    print(f"Cidade: {cidade} | Latitude: {lat} | Longitude: {lon}")