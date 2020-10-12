    def keyPressEvent(self, event):
        '''
        Function: keyPressEvent(self, event)
        Usage: Add response to keyboard events
        Note: F1 - 16777264
              F2 - 16777265
              F3 - 16777266
              F4 - 16777267
              F5 - 16777268
              F6 - 16777269
              '.' - 46
              Enter - 16777220
              Backspace - 16777219 *
        '''
        # team_set is False - unset
        # Start insert the card number and
        # change the focus on which control
        '''
        if self.team_set is False and self.team_insert is False and event.key(
        ) == 46:
            self.team_insert = True
            self.team_box.clear()

        # Inserting and Get which user the input key represents
        if self.team_set is False and self.team_insert is True:
            if event.key() == 16777266:
                self.team_now = 1  # team A
                self.team_box.setFocus()
            elif event.key() == 16777267:
                self.team_now = 2
                self.team_box.setFocus()
            elif event.key() == 16777268:
                self.team_now = 3
                self.team_box.setFocus()
            elif event.key() == 16777269:
                self.team_now = 4
                self.team_box.setFocus()

        # End input and handle events
        if self.team_set is False and self.team_insert is True and event.key(
        ) == 16777220:
            self.team_insert = False
            self.focus_box.setFocus()  # disable lineedit box
            if self.team_now == 1:  # set four team id
                self.team_A_id = int(self.team_box.text())
                self.team_box.clear()
            elif self.team_now == 2:
                self.team_B_id = int(self.team_box.text())
                self.team_box.clear()
            elif self.team_now == 3:
                self.team_C_id = int(self.team_box.text())
                self.team_box.clear()
            elif self.team_now == 4:
                self.team_D_id = int(self.team_box.text())
                self.team_box.clear()
            if self.team_A_id:  # all is set
                if self.team_B_id:
                    if self.team_C_id:
                        if self.team_D_id:
                            self.team_set = True  # all the team is set well
                            self.Set_team()'''

        # team_set is True - set well
        if self.team_set is True:
            if self.step == -1:  # step-1: clear all and wait for insert
                self.team_box.clear()
                self.team_box.setFocus()
                self.step = 0
            if self.step == 0:  # step0: get the player1`s id / know add or sub
                if event.key() == 16777264:  # add
                    self.symbol = 1
                    self.focus_box.setFocus()
                    self.player1_id = int(self.team_box.text())
                    self.team_box.clear()
                    self.step = 1
                elif event.key() == 16777265:  # sub
                    self.symbol = -1
                    self.focus_box.setFocus()
                    self.player1_id = int(self.team_box.text())
                    self.team_box.clear()
                    self.step = 1
            if self.step == 1:  # step1: get the player2`s id
                if event.key() == 16777266:
                    self.player2_id = self.team_A_id
                    self.team_box.setFocus()
                    self.step = 2
                elif event.key() == 16777267:
                    self.player2_id = self.team_B_id
                    self.team_box.setFocus()
                    self.step = 2
                elif event.key() == 16777268:
                    self.player2_id = self.team_C_id
                    self.team_box.setFocus()
                    self.step = 2
                elif event.key() == 16777269:
                    self.player2_id = self.team_D_id
                    self.team_box.setFocus()
                    self.step = 2
            if self.step == 2:  # step2: get the number to add / sub
                if event.key() == 16777220:
                    self.number = int(self.team_box.text())
                    self.team_box.clear()
                    self.focus_box.setFocus()
                    self.Solve()
                    self.step = -1
