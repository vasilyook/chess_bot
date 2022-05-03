# можно вынести сюда функцию и запускать в боте!
from bots.models import User, Division, Game

def read_file(self):
	text_file = open("command.txt", 'r+')
	command = text_file.readline()
	text_file.close()
	# print(command)
	return command

def write_file(self, command):
	text_file = open("command.txt", 'w+')
	text_file.write(command)
	text_file.close()

# username = match_res.group('player_name')

def check_user(username):
	if User.objects.filter(name=username).count() == 0:
		user = User(name = username)
		user.save()
		return user.id
	return User.objects.get(name=username).id


def check_division(division):
	if Division.objects.filter(name=division).count() == 0:
		division = Division(name=division)
		division.save()
		return division.id
	return Division.objects.get(name=division).id

def store_game(match_res):
	div_id = check_division(match_res.group('division'))
	pl_id = check_user(match_res.group('player_name'))
	opp_id = check_user(match_res.group('opponent_name'))
	game = Game(tour=match_res.group('tour'), division_id=div_id, player_id=pl_id, opponent_id=opp_id, player_score=float(match_res.group('player_score')), opponent_score=float(match_res.group('opponent_score')), links=match_res.group('links'))
	game.save()
	return game.links
	# q = Question(quвestion_text="What's new?", pub_date=timezone.now())
	# q.save()