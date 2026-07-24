function sortTeamRank(t1Name, t2Name, matchResults) {
  let { points: t1Points, scored: t1Scored, conceded: t1Conceded } = matchResults[t1Name];
  let { points: t2Points, scored:t2Scored, conceded: t2Conceded} = matchResults[t2Name];

  if (t1Points === t2Points) {
    let t1Diff = t1Scored - t1Conceded;
    let t2Diff = t2Scored - t2Conceded;

    if (t1Diff === t2Diff) {
      return t2Scored - t1Scored;
    }
    return t2Diff - t1Diff;
  }

  return t2Points - t1Points;
}

function determineQualifiers(groupResults) {
  if (groupResults.length === 0) {
    return [];
  }

  let matchResults = {};
  groupResults.forEach(result => {
    let { team1: t1Name, score1: t1Score, team2: t2Name, score2: t2Score } = result;
    
    if (!matchResults[t1Name]) {
      matchResults[t1Name] = { 
        points: 0, scored: 0, conceded: 0
      }
    }

    if (!matchResults[t2Name]) {
      matchResults[t2Name] = { 
        points: 0, scored: 0, conceded: 0
      }
    }

    if (t1Score > t2Score) {
      matchResults[t1Name].points += 3;
    } else if (t1Score === t2Score) {
      matchResults[t1Name].points += 1;
      matchResults[t2Name].points += 1;
    } else {
      matchResults[t2Name].points += 3;
    }

    matchResults[t1Name].scored += t1Score;
    matchResults[t1Name].conceded += t2Score;

    matchResults[t2Name].scored += t2Score;
    matchResults[t2Name].conceded += t1Score;
  })

  let countryNames = Object.keys(matchResults);
  countryNames.sort((t1Name, t2Name) => sortTeamRank(t1Name, t2Name, matchResults));

  return countryNames.slice(0, 2);
}

// edge case
console.log(determineQualifiers([])); // []

// Mexico, Canda, Argentina, Poland 
const groupAResults = [
  { team1: 'Mexico', score1: 2, team2: 'Canada', score2: 2 },
  { team1: 'Argentina', score1: 3, team2: 'Poland', score2: 0 },
  { team1: 'Mexico', score1: 1, team2: 'Argentina', score2: 2 },
  { team1: 'Canada', score1: 0, team2: 'Poland', score2: 0 },
  { team1: 'Poland', score1: 1, team2: 'Mexico', score2: 2 },
  { team1: 'Argentina', score1: 4, team2: 'Canada', score2: 1 },
];
console.log(determineQualifiers(groupAResults)); // Expected: ['Argentina', 'Mexico']

// USA, England, Wales, Iran
const groupBResults = [
  { team1: 'USA', score1: 1, team2: 'England', score2: 1 },
  { team1: 'Wales', score1: 0, team2: 'Iran', score2: 2 },
  { team1: 'USA', score1: 2, team2: 'Iran', score2: 0 },
  { team1: 'England', score1: 3, team2: 'Wales', score2: 0 },
];
console.log(determineQualifiers(groupBResults)); // Expected: ['England', 'USA']

// Brazil, Japan, Kenya, Norway
const groupCResults = [
  { team1: 'Brazil', score1: 2, team2: 'Japan', score2: 2 },
  { team1: 'Kenya', score1: 1, team2: 'Norway', score2: 1 },
  { team1: 'Brazil', score1: 3, team2: 'Kenya', score2: 1 },
  { team1: 'Japan', score1: 2, team2: 'Norway', score2: 0 },
  { team1: 'Brazil', score1: 1, team2: 'Norway', score2: 0 },
  { team1: 'Japan', score1: 1, team2: 'Kenya', score2: 0 },
];
console.log(determineQualifiers(groupCResults)); // Expected: ['Brazil', 'Japan']

/*
Brazil: {point: 7, scored: 6, conceded: 3} diff: 3 
Japan: {point: 7, scored: 5, conceded: 2} diff: 3 
Kenya: {point: 1, scored: 2, conceded: 5}
Norway: {point: 1, scored: 1, conceded: 4}
Top two teams have 1) same points, 2) same diff
We order them by # goals scored.
#1: Brazil (scored: 6)
#2: Japan (scored: 5)
*/