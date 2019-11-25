from abc import ABCMeta, abstractmethod

class Play(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class New_game(Play):
    def __init__(self,play):
        self.pl=play

    def execute(self):
        self.pl.New_game()

class Continue(Play):
    def __init__(self,play):
        self.pl=play

    def execute(self):
        self.pl.Continue()

class Options(Play):
    def __init__(self,play):
        self.pl=play

    def execute(self):
        self.pl.Options()

class Exit(Play):
    def __init__(self,play):
        self.pl=play

    def execute(self):
        self.pl.Exit()

class Start:
    def New_game(self):
        print('New Game')

    def Continue(self):
        print('Continue')

    def Options(self):
        print('Options')

    def Exit(self):
        print('Exit')

class shop:
    def __init__(self):
        self._playQeueue=[]

    def requestPlay(self,play):
        self._playQeueue.append(play)
        play.execute()

if __name__ == '__main__':
    st=Start()
    tr_new_game=New_game(st)
    tr_continue=Continue(st)
    tr_options=Options(st)
    tr_exit=Exit(st)

    sp=shop()
    sp.requestPlay(tr_new_game)
    sp.requestPlay(tr_continue)
    sp.requestPlay(tr_options)
    sp.requestPlay(tr_exit)
    

    
