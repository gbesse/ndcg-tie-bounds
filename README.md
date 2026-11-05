# ndcg-tie-bounds

## Français

Borner NDCG sur les permutations de scores ex æquo.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m ndcg_tie_bounds examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Bornes par réarrangement et espérance uniforme dans chaque groupe ex æquo, y compris un groupe coupé par k ; gains2^rel−1 et réduction log2.

### Limites

Jugements complets fournis, égalité exacte des scores ; pas de tolérance implicite ni preuve de qualité sur des requêtes réelles.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Bound NDCG over tied-score permutations.

Synthetic data; no network access or secret required.

```sh
python -m ndcg_tie_bounds examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Rearrangement bounds and uniform expectation within each tie group, including groups cut by k; gains2^rel−1 and log2 discount.

### Limits

Supplied complete judgments, exact score equality; no implicit tolerance or proof of quality on real queries.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Acotar NDCG sobre permutaciones de puntuaciones empatadas.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m ndcg_tie_bounds examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Cotas por reordenación y esperanza uniforme en grupos empatados, incluso cortados por k; ganancias2^rel−1 y descuento log2.

### Límites

Juicios completos aportados, igualdad exacta de puntuaciones; sin tolerancia implícita ni prueba de calidad en consultas reales.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ndcg_score.html
