/**

1、只出现一次的数字
    作者: VAME

*/

import java.util.Scanner;

public class Main {
    public static int singleNumber(int[] nums) {
        int result = 0;
        for (int num : nums) {
            result ^= num;
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("输入数组元素（以空格分隔）：");
        String[] input = scanner.nextLine().split("\\s+");
        int[] nums = new int[input.length];

        for (int i = 0; i < input.length; i++) {
            nums[i] = Integer.parseInt(input[i]);
        }

        int result = singleNumber(nums);
        System.out.println("输出：" + result);
    }
}
