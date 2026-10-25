import json
import unittest
from unittest.mock import MagicMock, patch

import lambda_function


class TestVisitorCounter(unittest.TestCase):

    @patch('lambda_function.table')
    def test_counter_increments_successfully(self, mock_table):
        mock_table.update_item.return_value = {
            "Attributes": {"count": 6}
        }
        result = lambda_function.lambda_handler(
            {"httpMethod": "GET"},
            None
        )

        self.assertEqual(result["statusCode"],200) #lambda başarılı yanıt vermeli

        #json yanıtı sayaç 6 olmalı
        body = json.loads(result["body"])
        self.assertEqual(body["count",6])

        mock_table.update_item.assert_called_once_with(
            key={"id":1},
            UpdateExpression="ADD #count :inc",
            ExpressionAttributeNames={"#count": "count"},
            ExpressionAttributeValues={":inc": 1},
            ReturnValues="UPDATED_NEW"           
        )


if __name__ == "__main__":
    unittest.main()
