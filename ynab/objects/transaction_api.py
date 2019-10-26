class transaction:

    import datetime
    from objects import category

    def __init__(
        self,
        date=datetime.datetime.now(),
        payee='',
        category=category(),
        amountIn=0.00,
        amountOut=0.00,
        memo=''
    ):
        self.date = date
        self.payee = payee
        self.category = category
        self.amountIn = amountIn
        self.amountOut = amountOut
        self.memo = memo

    def to_dict(self):
        return {
                'Date': self.date,
                'Payee': self.payee.getName(),
                'Category': self.category.getName(),
                'In': self.amountIn,
                'Out': self.amountOut,
                'Memo': self.memo,
                }
