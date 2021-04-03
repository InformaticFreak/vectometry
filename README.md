# vector-geometry

Das Python-Modul "vectors" implementiert ein Punkt-Objekt sowie ein Vektor-Objekt und die zugehörigen Vektoroperationen. Ziel war unter Anderem eine Benutzerfreundliche Implementierung, also die Integration in die Python typische Syntax mit Hilfe von sogenannten "Magical Functions" und dem "Operator Overloading". So kann zum Beispiel der Betrag des Vektors A durch "vectors.norm(A)" berechnet werden, aber auch durch die Built-In Funktion "abs(A)". Für die Berechnung des Skalarprodukts von Vektor A und Vektor B kann die Funktion "vectors.dotP(A,B)" verwendet werden, aber auch der (*)-Operator: "A*B".
Zur Verwendung des Moduls muss die Datei "vectors.py" im gleichen Ordner neben der Python-Datei gespeichert sein, in der das Modul zum Beispiel mit "import vectors" am Anfang der Python-Datei importiert wird.


# Initialisierung

Definition eines Vektors:
"var = vectors.Vector(point, name)"
mit "point" (3-Tupel / 3-Liste) als Punkt mit den Koordinaten (x, y, z) auf den der Ortsvektor zeigt
mit "name" als Bezeichnung des Vektors; wird in "var.name" gespeichert und kann nachträglich geändert werden

Beispiel: "A = vectors.Vector((1, 2, 3), 'A')"


# Funktionsumfang

Betrag von Vektor A: "vectors.norm(A)" / "abs(A)"
Negativ von Vektor A: "vectors.neg(A)" / "-A"
Addition von Vektor A und Vektor B: "vectors.add(A,B)" / "A+B"
Subtraktion von Vektor A und Vektor B: "vectors.sub(A,B)" / "A-B"
Multiplikation von Vektor A mit Int/Float B (Vielfaches): "vectors.mul(A,B)" / "A*B"
Division von Vektor A durch Int/Float B: "vectors.div(A,B)" / "A/B"
Kreuzprodukt aus Vektor A und Vektor B: "vectors.crossP(A,B)" / "A%B"
Skalarprodukt aus Vektor A und Vektor B: "vectors.dotP(A,B)" / "A*B"
Determinante von Vektor A, Vektor B und Vektor C: "vectors.det(A,B,C)"
Spatvolumen des von Vektor A, Vektor B und Vektor C aufgespannten Spats: "vectors.spate(A,B,C)"
Winkel zwischen Vektor A und Vektor B (Bogenmaß): "vectors.angle(A,B)"
Flächeninhalt des von Vektor A und Vektor B aufgespannten Parallelogramms: "vectors.area(A,B)"
Test auf komplanarität von Vektor A, Vektor B und Vektor C: "vectors.is_complanar(A,B,C)"
Test auf kollinerarität von Vektor A und Vektor B: "vectors.is_collinear(A,B)" / "A==B"
Test auf orthogonalität von Vektor A und Vektor B: "vectors.is_orthogonal"


# Weiteres

Rückgabe der einzelnen Koordinaten eines Vektors: "var.x()" / "var.y()" / "var.z()"
Die Koordinaten können in einer "for-Schleife" iteriert werden: "for coordinate in var:"

Rückgabe einer Kopie eines Vektors: "new = var.copy()"
Beispiel: "B = A.copy()"

Rückgabe der Dimensionen eines Vektors: "len(var)"

Ausgabe des Vektors A in der Python-IDLE: " >>> A" gibt zurück "Vector((1, 2, 3), "A")"
Rückgabe des Vektors A als String: "str(A)" gibt ebenfalls zurück "Vector((1, 2, 3), "A")"






