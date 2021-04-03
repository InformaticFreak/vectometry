# vector-geometry

Das Python-Modul **vectors** implementiert ein Punkt-Objekt sowie ein Vektor-Objekt und die zugehörigen Vektoroperationen. Ziel war unter Anderem eine Benutzerfreundliche Implementierung, also die Integration in die Python typische Syntax mit Hilfe von sogenannten *Magical Functions* und dem *Operator Overloading*. So kann zum Beispiel der Betrag des Vektors A durch `vectors.norm(A)` berechnet werden, aber auch durch die Built-In Funktion `abs(A)`. Für die Berechnung des Skalarprodukts von Vektor A und Vektor B kann die Funktion `vectors.dot(A,B)` verwendet werden, aber auch der (`*`)-Operator: `A*B`.


## Initialisierung

Definition eines Vektors: `vec = vectors.Vector(*args)`
Wobei `*args` den Punkt auf den der Orstvektor zeigt enthält. Dieser Punkt kann als Liste/Tupel mit drei Elementen übergeben werden; als einzelne Werte; als ein Point-Objekt oder als Differenz aus zwei Point-Objekten.
Beispiele:
`vectors.Vector(1, 2, 3)`
`vectors.Vector((1, 2, 3))`
`vectors.Vector([1, 2, 3])`
`vectors.Vector(Point(1, 2, 3))`
`vectors.Vector(Point(4, 5, 6) - Point(1, 2, 3))`

Definition eines Punktes: `pnt = vectors.Point(*args)`
Hier entält `*args` die Koordinaten des Punktes als Liste/Tupel mit drei Elementen oder als einzelne Werte.
Beispiele:
`vectors.Point(1, 2, 3)`
`vectors.Point((1, 2, 3))`
`vectors.Point([1, 2, 3])`


## Funktionsumfang

Betrag von Vektor A: `vectors.norm(A)` / `abs(A)`
Negativ von Vektor A: `vectors.neg(A)` / `-A`
Addition von Vektor A und Vektor B: `vectors.add(A,B)` / `A+B`
Subtraktion von Vektor A und Vektor B: `vectors.sub(A,B)` / `A-B`
Multiplikation von Vektor A mit Int/Float B (Vielfaches): `vectors.mul(A,B)` / `A*B`
Division von Vektor A durch Int/Float B: `vectors.div(A,B)` / `A/B`
Kreuzprodukt aus Vektor A und Vektor B: `vectors.cross(A,B)` / `A%B`
Skalarprodukt aus Vektor A und Vektor B: `vectors.dot(A,B)` / `A*B`
Determinante von Vektor A, Vektor B und Vektor C: `vectors.det(A,B,C)`
Spatvolumen des von Vektor A, Vektor B und Vektor C aufgespannten Spats: `vectors.spate(A,B,C)`
Winkel zwischen Vektor A und Vektor B (Bogenmaß): `vectors.angle(A,B)`
Flächeninhalt des von Vektor A und Vektor B aufgespannten Parallelogramms: `vectors.area(A,B)`
Test auf komplanarität von Vektor A, Vektor B und Vektor C: `vectors.is_complanar(A,B,C)`
Test auf kollinerarität von Vektor A und Vektor B: `vectors.is_collinear(A,B)` / `A==B`
Test auf orthogonalität von Vektor A und Vektor B: `vectors.is_orthogonal`

Differenz aus zwei Punkten A und B: `vectors.sub(B,A)` / `B-A` gibt Differenzvektor zurück `vectors.Vector(B-A)`


## Weiteres

Rückgabe der einzelnen Koordinaten eines Vektors oder Punktes: `var.x()` / `var.y()` / `var.z()`
Die Koordinaten können in einer `for-Schleife` iteriert werden: `for coordinate in var:`

Rückgabe einer Kopie eines Vektors oder Punktes: `var_new = var.copy()`
Beispiel: `B = A.copy()`

Rückgabe der Dimensionen eines Vektors oder Punktes: `len(var)`

Ausgabe des Vektors oder Punktes A in der Python-IDLE ` >>> A` oder als String `str(A)`: gibt zurück `Vector(1, 2, 3)` bzw. `Point(1, 2, 3)`

