// TITLE: GOOD VS EVIL
// TASK : Middle Earth is about to go to war. The forces of good will have many battles with the forces of evil. 
//        Different races will certainly be involved. Each race has a certain worth when battling against others. 
//        Although weather, location, supplies and valor play a part in any battle, if you add up the worth of the side of good and 
//        compare it with the worth of the side of evil, the side with the larger worth will tend to win.
// Source: https://www.codewars.com/kata/52761ee4cffbc69732000738
// 21 - 22 February 2024

import java.util.Arrays;

public class J_0039_good_vs_evil {
    // 1st method - very long but just do it [THIS CODE IS WRONG!!]
    // public static String battle(String goodAmounts, String evilAmounts) {
    //     String[] goodTroops = new String[6];
    //     String[] evilTroops = new String[7];
    //     String[] tempStrings = {"", ""};
    //     int j = 0;
    //     for (int i = 0; i < goodAmounts.length(); i++) {
    //         if (goodAmounts.charAt(i) != ' ') {
    //             tempStrings[0] += goodAmounts.charAt(i);
    //             if (i == goodAmounts.length() - 1) {
    //                 goodTroops[j] = tempStrings[0];
    //             }
    //         } else {
    //             goodTroops[j] = tempStrings[0];
    //             tempStrings[0] = "";
    //             j++;
    //         }
    //     }

    //     j = 0;
    //     for (int i = 0; i < evilAmounts.length(); i++) {
    //         if (evilAmounts.charAt(i) != ' ') {
    //             tempStrings[1] += evilAmounts.charAt(i);
    //             if (i == evilAmounts.length() - 1) {
    //                 evilTroops[j] = tempStrings[1];
    //             }
    //         } else {
    //             evilTroops[j] = tempStrings[1];
    //             tempStrings[1] = "";
    //             j++;
    //         }
    //     }

    //     // Convert the troops to integer
    //     int[] goodTroopsInt = new int[goodTroops.length];
    //     int[] evilTroopsInt = new int[evilTroops.length];

    //     for (int i = 0; i < goodTroops.length; i++) {
    //         goodTroopsInt[i] = Integer.parseInt(goodTroops[i]);
    //     }

    //     for (int i = 0; i < evilTroopsInt.length; i++) {
    //         evilTroopsInt[i] = Integer.parseInt(evilTroops[i]);
    //     }

    //     int goodTroopsAmount = 0, evilTroopsAmount = 0;
    //     for (int i : goodTroopsInt) {
    //         goodTroopsAmount += i;
    //     }

    //     for (int i : evilTroopsInt) {
    //         evilTroopsAmount += i;
    //     }

    //     if (goodTroopsAmount > evilTroopsAmount) {
    //         return "Battle Result: Good triumphs over Evil";
    //     } else if (evilTroopsAmount > goodTroopsAmount) {
    //         return "Battle Result: Evil eradicates all trace of Good";
    //     } else {
    //         return "Battle Result: No victor on this battle field";
    //     }
    // }

    // // 2nd method - using String.split()
    // public static String battle(String goodAmounts, String evilAmounts) {
    //     String[] goodTroops = goodAmounts.split(" ");
    //     String[] evilTroops = evilAmounts.split(" ");

    //     // Convert the troops to integer
    //     int[] goodTroopsInt = new int[goodTroops.length];
    //     int[] evilTroopsInt = new int[evilTroops.length];

    //     for (int i = 0; i < goodTroops.length; i++) {
    //         goodTroopsInt[i] = Integer.parseInt(goodTroops[i]);
    //     }

    //     for (int i = 0; i < evilTroopsInt.length; i++) {
    //         evilTroopsInt[i] = Integer.parseInt(evilTroops[i]);
    //     }

    //     // Count the total points of troops
        // int goodTroopsAmount = 0, evilTroopsAmount = 0;
        // goodTroopsAmount += goodTroopsInt[0] * 1;
        // goodTroopsAmount += goodTroopsInt[1] * 2;
        // goodTroopsAmount += goodTroopsInt[2] *3;
        // goodTroopsAmount += goodTroopsInt[3] * 3;
        // goodTroopsAmount += goodTroopsInt[4] * 4;
        // goodTroopsAmount += goodTroopsInt[5] * 10;

        // evilTroopsAmount += evilTroopsInt[0] * 1;
        // evilTroopsAmount += evilTroopsInt[1] * 2;
        // evilTroopsAmount += evilTroopsInt[2] * 2;
        // evilTroopsAmount += evilTroopsInt[3] * 2;
        // evilTroopsAmount += evilTroopsInt[4] * 3;
        // evilTroopsAmount += evilTroopsInt[5] * 5;
        // evilTroopsAmount += evilTroopsInt[6] * 10;

    //     if (goodTroopsAmount > evilTroopsAmount) {
    //         return "Battle Result: Good triumphs over Evil";
    //     } else if (evilTroopsAmount > goodTroopsAmount) {
    //         return "Battle Result: Evil eradicates all trace of Good";
    //     } else {
    //         return "Battle Result: No victor on this battle field";
    //     }
    // }

    // 3rd method - just another version
    public static String battle(String goodAmounts, String evilAmounts) {
        int[] goodAmountsInt = Arrays.stream(goodAmounts.split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] evilAmountsInt = Arrays.stream(evilAmounts.split(" ")).mapToInt(Integer::parseInt).toArray();


        // Count the total points of trrops
        int goodTroopsAmount = 0, evilTroopsAmount = 0;
        for (int i = 0; i < goodAmountsInt.length; i++) {
            if (i < 3) {
                goodTroopsAmount += goodAmountsInt[i] * (i + 1);
            } else if (i == 3 || i == 4) {
                goodTroopsAmount += goodAmountsInt[i] * i;
            } else {
                goodTroopsAmount += goodAmountsInt[i] * (i * 2);
            }
        }

        for (int i = 0; i < evilAmountsInt.length; i++) {
            if (i <= 1) {
                evilTroopsAmount += evilAmountsInt[i] * (i + 1);
            } else if (i == 2 || i == 5) {
                evilTroopsAmount += evilAmountsInt[i] * i;
            } else if (i == 3 || i == 4) {
                evilTroopsAmount += evilAmountsInt[i] * (i -1);
            } else {
                evilTroopsAmount += evilAmountsInt[i] * 10;
            }
        }

        // Return the result
        if (goodTroopsAmount > evilTroopsAmount) {
            return "Battle Result: Good triumphs over Evil";
        } else if (evilTroopsAmount > goodTroopsAmount) {
            return "Battle Result: Evil eradicates all trace of Good";
        } else {
            return "Battle Result: No victor on this battle field";
        }
    }

    public static void main(String[] args) {
        // Testing
        System.out.println(battle("1 1 1 1 1 1", "1 1 1 1 1 1 1"));
        System.out.println(battle("0 0 0 0 0 10", "0 1 1 1 1 0 0"));
        System.out.println(battle("7209 8612 6429 2643 7560 5210", "5687 9447 500 287 9588 2361 8608"));
        System.out.println(battle("7368 8609 4020 1765 3834 6092", "101 5800 530 7801 960 3495 8477"));
    }
}
