function isAlpha(char) {
  if ((char >= 'a' && char <= 'z') || (char >= 'A' && char <= 'Z')) {
    return true;
  } else {
    return false;
  }
}

function cleanUp(sentence) {
  let result = '';
  for (let i = 0; i < sentence.length; i += 1) {
    if (isAlpha(sentence[i])) {
      result += sentence[i];
      continue;
    }

    if (result[result.length - 1] !== ' ') {
      result += ' ';
    }
  }
  
  return result;
}


console.log(cleanUp("---what's my +*& line?"));    // " what s my line "