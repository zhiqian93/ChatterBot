from mock import MagicMock
from chatterbot.logic import BestMatch
from chatterbot.conversation import Statement
from tests.base_case import ChatBotTestCase


class BestMatchTestCase(ChatBotTestCase):
    """
    Unit tests for the BestMatch logic adapter.
    """

    def setUp(self):
        super(BestMatchTestCase, self).setUp()
        self.adapter = BestMatch()
        self.adapter.set_chatbot(self.chatbot)

    def test_get_class_namespace(self):
        """
        Test that the namespace string is returned for the class.
        """
        result = self.adapter.get_class_namespace()
        self.assertEqual(result, 'chatterbot.logic.best_match.BestMatch')

    def test_no_choices(self):
        """
        An exception should be raised if there is no data in the database.
        """
        self.adapter.chatbot.storage.filter = MagicMock(return_value=[])
        self.adapter.chatbot.storage.count = MagicMock(return_value=0)

        statement = Statement('What is your quest?')

        with self.assertRaises(BestMatch.EmptyDatasetException):
            self.adapter.get(statement)
