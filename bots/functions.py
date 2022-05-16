# можно вынести сюда функцию и запускать в боте!
from bots.models import User, Division, Game, TelegramUser
errors = []

# username = match_res.group('player_name')

def create_user(username):
	user = User(name = username)
	user.save()
	return user.id

def create_division(division):
	division = Division(name=division)
	division.save()
	return division.id

def create_telegram_user(tg_name, tg_id):
	tg_user = TelegramUser(name=tg_name, telegram_id=tg_id)
	tg_user.save()
	return tg_user.id

def cut_links(links):
	links = links.replace('https://lichess.org/', '')
	return links

def check_user(username):
	username = username.replace('\n', '').strip()
	if User.objects.filter(name=username).count() == 0:
		error = 'Имени "' + username + '" нет в списке игроков.'
		return errors.append(error)
	return User.objects.get(name=username).id

def check_division(division):
	if Division.objects.filter(name=division).count() == 0:
		error = 'Дивизиона "' + division + '" нет в списке.'
		return errors.append(error)
	return Division.objects.get(name=division).id


# check tg_user and create him if he isn't
def check_telegram_user(tg_name, tg_id):
	if TelegramUser.objects.filter(telegram_id=tg_id).count() == 0:
		return create_telegram_user(tg_name, tg_id)
	return TelegramUser.objects.get(telegram_id=tg_id).id

def update_last_command(pk, command):
	user = TelegramUser.objects.get(id=pk)
	user.last_command = command
	user.save()

def store_game(match_res):
	errors.clear()
	div_id = check_division(match_res.group('division'))
	pl_id = check_user(match_res.group('player_name'))
	opp_id = check_user(match_res.group('opponent_name'))
	cutting_links = cut_links(match_res.group('links'))
	pl_score = match_res.group('player_score').replace(',','.')
	opp_score = match_res.group('opponent_score').replace(',','.')
	if len(errors) != 0:
		print(errors)
		# write_file(self, '\n'.join(errors))
		return '\n'.join(errors)
	try:
		game = Game(tour=match_res.group('tour'), division_id=div_id, player_id=pl_id, opponent_id=opp_id, player_score=pl_score, opponent_score=opp_score, links=cutting_links)
		game.clean_fields()
		game.save()
	except Exception as e:
		return str(e)
	return 'Ваша игра сохранена.'
