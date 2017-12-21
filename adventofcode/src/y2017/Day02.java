
package y2017;

import java.util.*;

public class Day02 {

	public static final String INPUT = "5 9 2 8\r\n" + "9 4 7 3\r\n" + "3 8 6 5";

	public static void part1() {
		long sum = 0;
		Scanner read = new Scanner(INPUT);
		while (read.hasNextLine()) {
			Scanner line = new Scanner(read.nextLine());
			int max = line.nextInt();
			int min = max;
			while (line.hasNext()) {
				int current = line.nextInt();
				max = (current > max) ? current : max;
				min = (current < min) ? current : min;
			}
			sum += (max - min);
			line.close();
		}
		read.close();
		System.out.println(sum);
	}

	public static void part2() {
		long sum = 0;
		Scanner read = new Scanner(INPUT);
		while (read.hasNextLine()) {
			String row = read.nextLine();
			Scanner read1 = new Scanner(row);
			int div = 0;
			while ((div == 0) && read1.hasNext()) {
				int current = read1.nextInt();
				Scanner read2 = new Scanner(row);
				while ((div == 0) && read2.hasNext()) {
					int compare = read2.nextInt();
					div = ((compare != current) && (compare % current == 0)) ? (compare / current) : 0;
				}
			}
			sum += div;
			read1.close();
		}
		read.close();
		System.out.println(sum);
	}

	public static void main(String[] args) {
		part1();
		part2();
	}

}
