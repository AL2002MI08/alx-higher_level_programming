#!/usr/bin/node

const argv = process.argv;

// Extract only Integers
const numsArgs = argv.filter(cur => !isNaN(cur)).map(cur => parseInt(cur));
if (!numsArgs[0] || numsArgs.length === 1) console.log(0);

// find max in array
const findMax = function (nums) {
  let max = nums[0];
  for (const num of nums) {
    if (max < num) max = num;
  }
  return max;
};

const findSecondBiggest = function (nums) {
  if (nums.length > 1) {
    // Remove the first biggest
    const newArr = nums.filter((cur, _, arr) => cur !== findMax(arr));
    console.log(findMax(newArr));
  }
};

findSecondBiggest(numsArgs);
