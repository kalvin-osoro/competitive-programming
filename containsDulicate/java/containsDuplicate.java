// Problem Statement
// Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

import java.util.HashSet;
import java.util.Set;

public class Solution {

  public boolean containsDuplicate(int[] nums) {
    // TODO: Write your code here
    for (int i=0; i<=nums.length-1; i++){
      for (int j = i+1; j<=nums.length-1; j++){
        if (nums[i] == nums[j]){
          return true;
        }

      }
    }
    return false;
  }
}


// test cases
// [1,2,3,4]
// [1,2,3,1]
// [3, 2, 6, -1, 2, 1]