import argparse
import random
import trace


class Point:
    """
    The Point class contains the x and y coordinates for a point
    """

    def __init__(self, x: int = 0, y: int = 0) -> None:
        """Initializes a new Point"""
        self.x = x
        self.y = y

    def __eq__(self, other: object, /) -> bool:
        """Compares this instance with another object"""
        if not isinstance(other, Point):
            return False

        return (self.x == other.x) and (self.y == other.y)

    def __hash__(self) -> int:
        """Returns a hash value for this instance"""
        return hash((self.x, self.y))

    def __str__(self) -> str:
        """Returns a string representaion of this instance"""
        return f"({self.x},{self.y})"

    def __repr__(self) -> str:
        """Returns a detailed representation of this instance"""
        return f"Point(x={self.x}, y={self.y})"


class Pair:
    """
    The Pair class contains two Points and the Manhattan Distance between them
    """

    def __init__(
        self, distance: int = 0, iPoint: Point = Point(), jPoint: Point = Point()
    ) -> None:
        """Initializes a new Pair"""
        self.distance = distance
        self.iPoint = iPoint
        self.jPoint = jPoint

    def __eq__(self, other: object, /) -> bool:
        """Compares this instance with another object"""
        if not isinstance(other, Pair):
            return False

        return (
            (self.distance == other.distance)
            and (self.iPoint == other.iPoint)
            and (self.jPoint == other.jPoint)
        )

    def __hash__(self) -> int:
        """Returns a hash value for the instance"""
        return hash((self.distance, self.iPoint, self.jPoint))

    def __str__(self) -> str:
        """Returns a string representaion of this instance"""
        return f"{self.distance}, {self.iPoint}, {self.jPoint}"

    def __repr__(self) -> str:
        """Returns a detailed representation of this instance"""
        return f"Pair(distance={self.distance}, iPoint={self.iPoint}, jPoint={self.jPoint})"


def manhattanDistance(iPoint: Point, jPoint: Point) -> int:
    """Computes Manhattan Distance between two points"""
    return abs(iPoint.x - jPoint.x) + abs(iPoint.y - jPoint.y)


def closestPairs(P, m) -> list[Pair]:
    """Performs the Closest Pairs algorithm"""
    # List containing sorted list of Pairs of Points
    # The list is the size of the number of closest Pairs desired
    D: list[Pair] = [Pair()] * m

    # Counter for the number of Pairs evaluated
    evaluatedPairs = 0

    # Counter for the number of shifts executed for insertion
    insertionShifts = 0

    for i in range(0, len(P) - 1):
        for j in range(i + 1, len(P)):
            # Calculate Manhattan Distance and create Pair for insertion
            d = manhattanDistance(P[i], P[j])
            pair = Pair(d, P[i], P[j])

            # Insert Pair into sorted array based on Manhattan Distance
            k = min([evaluatedPairs, m]) - 1
            if evaluatedPairs < m or pair.distance < D[k].distance:
                while k >= 0 and pair.distance < D[k].distance:
                    if k < m - 1:
                        D[k + 1] = D[k]
                    k -= 1

                    # Increment the counter for the number of insertion shifts
                    insertionShifts += 1

                D[k + 1] = pair

            # Increment the counter for the number of evaluated pairs
            evaluatedPairs += 1

    # Print algorithm results
    print(f"Evaluated Pairs: {evaluatedPairs}")
    print(f"Insertion Shifts: {insertionShifts}")

    # Return
    return D[:min([evaluatedPairs, m])]


def generateInput(n: int) -> list[Point]:
    """Generates a list of n unique points"""
    # Use a set to force unique elements
    points = set()

    # Loop until points has n elements
    while len(points) < n:
        # Use n as upper bound so we don't run out of numbers
        points.add(Point(random.randint(0, n), random.randint(0, n)))

    # Make points into a list to keep order consistent
    points = list(points)

    return points


def getArguments() -> argparse.Namespace:
    """Get the program's arguments"""
    # Program information
    parser = argparse.ArgumentParser(
        prog="Closest-Pairs",
        description="Executes the Closest Pairs algorithm",
    )

    # Run a trace
    parser.add_argument(
        "-t",
        "--trace",
        action="store_true",
        help="Runs a trace on the algorithm",
    )

    # Specify specific input file if desired
    parser.add_argument(
        "-i",
        "--input",
        action="store",
        default="input.txt",
        help="Specify input file name; can be used for specific inputs when the "
        "'P' flag is omitted, otherwise will save input file to given location",
    )

    # Number of Points to use in the Closest Pairs algorithm
    parser.add_argument(
        "-P",
        "--numPoints",
        action="store",
        default=0,
        help="The number of points to use in the Closest Pairs algorithm",
    )

    # Number of Closests Pairs to file in the Closest Pairs algorithm
    parser.add_argument(
        "-m",
        "--numPairs",
        action="store",
        default=0,
        help="The number of closest pairs to look for in the Closest Pairs algorithm",
    )

    # Output file
    parser.add_argument(
        "-o",
        "--output",
        action="store",
        default="output.txt",
        help="Specify output file name",
    )

    return parser.parse_args()


def main(args: argparse.Namespace) -> None:
    P: list[Point] = []
    m: int = 0
    D: list[Pair] = []

    # Generate
    if args.numPoints is not None:
        with open(args.input, "w") as f:
            for point in generateInput(int(args.numPoints)):
                print(point, file=f)

    # Input
    try:
        with open(args.input, "r") as f:
            for line in f.readlines():
                P.append(Point(*eval(line)))
    except FileNotFoundError:
        print(f"Could not find {args.input}")
        exit()

    # Number of closest pairs
    m = int(args.numPairs)

    # Run the Closest Pairs algorithm
    D = closestPairs(P, m)

    # Save the output
    with open(args.output, "w") as f:
        for pair in D:
            print(pair, file=f)


if __name__ == "__main__":
    # Get the program's arguments
    args = getArguments()

    # Run a trace
    if args.trace:
        # Create Trace object
        tracer = trace.Trace(
            ignoredirs=[],
            trace=0,
            count=1,
        )

        # Run trace
        tracer.run("main(args)")

        # Make a report
        r = tracer.results()
        r.write_results(show_missing=True, coverdir="traceOutput")

    # Run normally
    else:
        main(args)
