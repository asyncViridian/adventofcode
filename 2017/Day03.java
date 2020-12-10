
package y2017;

import java.util.*;

public class Day03 {

	public static final int INPUT = 347991;
	public static final int NUM_CORNERS = 4;

	public static void part1() {
		int diagonalRoot = 1;
		while ((diagonalRoot * diagonalRoot) < INPUT) {
			diagonalRoot += 2;
		}
		int minCornerDistance = diagonalRoot;
		for (int i = (NUM_CORNERS - 1); (i >= 0) && (minCornerDistance == diagonalRoot); i--) {
			int testing = (diagonalRoot * diagonalRoot) - (i * (diagonalRoot - 1));
			if (testing >= INPUT) {
				int downDist = testing - INPUT;
				int upDist = diagonalRoot - 1 - downDist;
				minCornerDistance = (downDist < minCornerDistance) ? downDist : minCornerDistance;
				minCornerDistance = (upDist < minCornerDistance) ? upDist : minCornerDistance;
			}
		}
		int steps = (diagonalRoot - 1) - minCornerDistance;
		System.out.println(steps);
	}

	public static void part2() {

	}

	public static void main(String[] args) {
		part1();
		part2();
	}

}
