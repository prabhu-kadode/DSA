function countChars(str) {
    const charCount = {};
  
    for (const char of str) {
      if (charCount[char]) {
        charCount[char] += 1;
      } else {
        charCount[char] = 1;
      }
    }
  
    return charCount;
  }
  
  // Example:
  const result = countChars('banana');
  console.log(result);
  