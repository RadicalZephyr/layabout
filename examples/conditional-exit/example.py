from layabout import Layabout

app = Layabout()


def main():
    magic = input('What is the magic word? ')
    print(f'Running until someone says "{magic}". Press Ctrl-C to quit.')

    def someone_says_the_magic_word(events):
        """
        Return False if someone said the magic word and the event loop stops.
        Otherwise we return True and the loop continues.
        """
        for event in events:
            if magic in event.get('text', ''):
                # Returning False here stops the event loop.
                return False

        # If we return True here then the loop continues.
        return True

    # This will run only until someone enters the magic word(s) into a channel.
    app.run(until=someone_says_the_magic_word)
    print(f'Someone said "{magic}"!')


if __name__ == '__main__':
    main()
