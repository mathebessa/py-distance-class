class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = float(km)

    def __str__(self) -> str:
        km_str = (
            str(int(self.km)) if self.km.is_integer() else str(self.km)
        )
        return f"Distance: {km_str} kilometers.\n"

    def __repr__(self) -> str:
        return f"Distance({self.km})"

    def __add__(self, other: "Distance") -> "Distance":
        return Distance(self.km + other.km)

    def __iadd__(self, other: "Distance") -> "Distance":
        self.km += other.km
        return self

    def __mul__(self, value: float) -> "Distance":
        return Distance(self.km * value)

    def __truediv__(self, value: float) -> "Distance":
        return Distance(self.km / value)

    def __lt__(self, other: "Distance") -> bool:
        return self.km < other.km

    def __gt__(self, other: "Distance") -> bool:
        return self.km > other.km

    def __eq__(self, other: "Distance") -> bool:
        return self.km == other.km

    def __le__(self, other: "Distance") -> bool:
        return self.km <= other.km

    def __ge__(self, other: "Distance") -> bool:
        return self.km >= other.km
