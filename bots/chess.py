from .bot import Bot
from .data import *
from .functions import *
from dotenv import load_dotenv
import os
import re

class Chess(Bot):
	_commands = ['start', 'help', 'add', 'games']
	@property
	def commands(self):
		return self._commands

	def add(self):
		return 	self.send_message(add_text, self.update.get_id())

	def answer(self):
		message = self.update.get_text()
		match_res = re.search(r'#?(?P<tour>\d+)\s*(?:тур)*\s*(?P<division>\w+)\s*\n*(?P<player_name>(?:\w+\s*)+)\s*-?:?\s*(?P<opponent_name>(?:\w+\s*)+)\s*\n*(?P<player_score>\d+\.?\,?\d?)-?:?\s*(?P<opponent_score>\d+\.?\,?\d?)\s*\n*(?P<links>https?:\/\/lichess\.org\/\w+\s*\n*(?:https?:\/\/lichess\.org\/\w+)*)', message)
		if match_res == None:
			return self.send_message('Сообщение не соответствует формату.' + add_text, self.update.get_id())
		text = store_game(match_res)
		return self.send_message(text, self.update.get_id())

	def games(self):
		return self.send_message(saved_games, self.update.get_id())

	def call_command(self):
		telegram_id = self.update.get_id()
		command = self.update.get_command()
		name = self.update.get_name()
		pk = check_telegram_user(name, telegram_id)
		update_last_command(pk, command)
		return super().call_command()

# load_dotenv()
# token = os.getenv("TOKEN")
# chess = Chess(token)
# chess.polling()