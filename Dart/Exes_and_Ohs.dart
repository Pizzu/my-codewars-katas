bool XO(str) {
  // your code here
  int xAmount = 0;
  int oAmount = 0;
  String lowerStr = str.toLowerCase();
  lowerStr.split("").forEach((char) {
    if (char == "x") {
      xAmount = xAmount + 1;
    } else if (char == "o") {
      oAmount = oAmount + 1;
    }
  });
  if (xAmount == 0 && oAmount == 0) {
    return true;
  } else {
    if (xAmount == oAmount) {
      return true;
    } else {
      return false;
    }
  }
}