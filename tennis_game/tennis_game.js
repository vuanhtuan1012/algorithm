/*
* @Author: anh-tuan.vu
* @Date:   2021-09-10 21:02:18
* @Last Modified by:   anh-tuan.vu
* @Last Modified time: 2021-09-10 21:08:13
*/

function score(nameP1, nameP2, wins){
	let score1 = 0
	let score2 = 0
	for (let name of wins) {
		if (name === nameP1) {
			score1 += 1
		}
		if (name === nameP2) {
			score2 += 1
		}
	}

	let translate_score = function(score){
		let point = 0
		switch (score){
			case 1:
				point = 15
				break
			case 2:
				point = 30
				break
			case 3:
				point = 40
				break
		}
		return point
	}

	let res = nameP1 + ' ' + translate_score(score1) + ' - '
			+ nameP2 + ' ' + translate_score(score2)
	let diff = score1 - score2
	if ((score1 == score2) && (score1 >= 3)) {
		res = 'DEUCE'
	}
	if ((diff == 1) && (score1 >= 4)){
		res = nameP1 + ' Advance'
	}
	if ((diff >= 2) && (score1 >= 4)){
		res = nameP1 + ' Wins'
	}
	if ((diff == -1) && (score2 >= 4)){
		res = nameP2 + ' Advance'
	}
	if ((diff <= -2) && (score2 >= 4)){
		res = nameP2 + ' Wins'
	}
	return res
}

let nameP1 = 'P1'
let nameP2 = 'P2'
let wins = ['P1', 'P1', 'P1', 'P2']
let result = score(nameP1, nameP2, wins)

document.getElementById('wins').innerText = wins.join(', ')
document.getElementById('result').innerText = result