import chess
import chess.pgn
import itertools
import csv            

def generateData(game):
    whiteElo = int(game.headers['WhiteElo'])
    node = game
    output = []
    turn = 1
    lastseen1 = [57,0]
    lastseen2 = [62,0]
    result = int(game.headers['Result'][0])
    while node.variations:
        next_node = node.variation(0)
        if(str(node.board().san(next_node.move))[0] == "N" and turn%2 ==0):
            row = [0] * 8
            row[0] = turn
            row[6] = whiteElo
            row[7] = result
            # If the knight is the left knight
            if next_node.move.from_square == lastseen1[0]: 
                # From Square
                FromSquare = next_node.move.from_square
                row[1] = chess.rank_index(FromSquare)
                row[2] = chess.file_index(FromSquare)
                # To Square
                ToSquare = next_node.move.to_square
                row[3] = chess.rank_index(ToSquare)
                row[4] = chess.file_index(ToSquare)
                # Updating lastseen vectors
                lastseen1[0] = next_node.move.to_square
                # Entering Time Spent
                timespent = turn - lastseen1[1]
                lastseen1[1] = turn/2
                row[5] = timespent/2
            # If the knight is the right knight
            if next_node.move.from_square == lastseen2[0]:
                FromSquare = next_node.move.from_square
                row[1] = chess.rank_index(FromSquare)
                row[2] = chess.file_index(FromSquare)
                # To Square
                ToSquare = next_node.move.to_square
                row[3] = chess.rank_index(ToSquare)
                row[4] = chess.file_index(ToSquare)
                # Updating lastseen vectors
                lastseen2[0] = next_node.move.to_square
                # Entering Time Spent
                timespent = turn - lastseen2[1]
                lastseen2[1] = turn/2
                row[5] = timespent/2 
            output.append(row)                  
        node = next_node
        turn += 1
    return(output)

def generateGMData(game):
    node = game
    output = []
    turn = 1
    lastseen1 = [57,0]
    lastseen2 = [62,0]
    result = int(game.headers['Result'][0])
    while node.variations:
        next_node = node.variation(0)
        if(str(node.board().san(next_node.move))[0] == "N" and turn%2 ==0):
            row = [0] * 7
            row[0] = turn
            row[6] = result
            # If the knight is the left knight
            if next_node.move.from_square == lastseen1[0]: 
                # From Square
                FromSquare = next_node.move.from_square
                row[1] = chess.rank_index(FromSquare)
                row[2] = chess.file_index(FromSquare)
                # To Square
                ToSquare = next_node.move.to_square
                row[3] = chess.rank_index(ToSquare)
                row[4] = chess.file_index(ToSquare)
                # Updating lastseen vectors
                lastseen1[0] = next_node.move.to_square
                # Entering Time Spent
                timespent = turn - lastseen1[1]
                lastseen1[1] = turn/2
                row[5] = timespent/2
            # If the knight is the right knight
            if next_node.move.from_square == lastseen2[0]:
                FromSquare = next_node.move.from_square
                row[1] = chess.rank_index(FromSquare)
                row[2] = chess.file_index(FromSquare)
                # To Square
                ToSquare = next_node.move.to_square
                row[3] = chess.rank_index(ToSquare)
                row[4] = chess.file_index(ToSquare)
                # Updating lastseen vectors
                lastseen2[0] = next_node.move.to_square
                # Entering Time Spent
                timespent = turn - lastseen2[1]
                lastseen2[1] = turn/2
                row[5] = timespent/2 
            output.append(row)                  
        node = next_node
        turn += 1
    return(output)

import csv
with open('D:/moves.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['turn','fromRank','fromFile','toRank','toFile','timeSpent','ELO','win'])
    for i in range(100000):
        gamedata = generateData(chess.pgn.read_game(test_pgn))
        for j in range(len(gamedata)):
            writer.writerow(gamedata[j])
        next(lightning_offsets)
        
        
carlsen_pgn = open("D:/STAT548/Project/DataProcessing/carlsen.pgn")
carlsen_offsets = chess.pgn.scan_offsets(carlsen_pgn)

with open('D:/carlsen.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['turn','fromRank','fromFile','toRank','toFile','timeSpent','ELO','win'])
    for i in range(1000):
        gamedata = generateGMData(chess.pgn.read_game(carlsen_pgn))
        for j in range(len(gamedata)):
            writer.writerow(gamedata[j])
        next(carlsen_offsets)
        
fischer_pgn = open("D:/STAT548/Project/DataProcessing/fischer.pgn")
fischer_offsets = chess.pgn.scan_offsets(carlsen_pgn)

with open('D:/fischer.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['turn','fromRank','fromFile','toRank','toFile','timeSpent','win'])
    for i in range(1000):
        gamedata = generateGMData(chess.pgn.read_game(fischer_pgn))
        for j in range(len(gamedata)):
            writer.writerow(gamedata[j])
        next(fischer_offsets)       
        
standard_pgn = open("D:/STAT548/Project/DataProcessing/standard2000.pgn")
standard_offsets = chess.pgn.scan_offsets(standard_pgn)

with open('D:/standard2000.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['turn','fromRank','fromFile','toRank','toFile','timeSpent','win'])
    for i in range(10000):
        gamedata = generateData(chess.pgn.read_game(standard_pgn))
        for j in range(len(gamedata)):
            writer.writerow(gamedata[j])
        if i%500 == 0:
            print i
        next(standard_offsets)       