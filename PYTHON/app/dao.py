def load_categories():
    return [{
        'id':1,
        'name':'mobile'
    },
        {
            'id': 2,
            'name': 'Tablet'
        }
    ]

def load_product(kw=None):
    products = [{
        'id':1,
        'name':'Iphone',
        'price': 2000000,
        'image': "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcQcdgusImUiCJArus7k1Xpq2XmobsujzRuNkZ-1YnxnWBULD8yyxQZ6GuD_i1VtWednLJc9KSAUrPxgazi0Ku3CirBSsl_yPmqaQq7oEfsPdmSoI9zi-SPiekBjJQ&usqp=CAc"
    }, {
        'id':2,
        'name':'Galaxy s20',
        'price': 2000000,
        'image': "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcQcdgusImUiCJArus7k1Xpq2XmobsujzRuNkZ-1YnxnWBULD8yyxQZ6GuD_i1VtWednLJc9KSAUrPxgazi0Ku3CirBSsl_yPmqaQq7oEfsPdmSoI9zi-SPiekBjJQ&usqp=CAc"
    }, {
        'id':3,
        'name':'Iphone',
        'price': 2000000,
        'image': "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcQcdgusImUiCJArus7k1Xpq2XmobsujzRuNkZ-1YnxnWBULD8yyxQZ6GuD_i1VtWednLJc9KSAUrPxgazi0Ku3CirBSsl_yPmqaQq7oEfsPdmSoI9zi-SPiekBjJQ&usqp=CAc"
    }, {
        'id':4,
        'name':'Iphone',
        'price': 2000000,
        'image': "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcQcdgusImUiCJArus7k1Xpq2XmobsujzRuNkZ-1YnxnWBULD8yyxQZ6GuD_i1VtWednLJc9KSAUrPxgazi0Ku3CirBSsl_yPmqaQq7oEfsPdmSoI9zi-SPiekBjJQ&usqp=CAc"
    }, {
        'id':5,
        'name':'Iphone',
        'price': 2000000,
        'image': "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcQcdgusImUiCJArus7k1Xpq2XmobsujzRuNkZ-1YnxnWBULD8yyxQZ6GuD_i1VtWednLJc9KSAUrPxgazi0Ku3CirBSsl_yPmqaQq7oEfsPdmSoI9zi-SPiekBjJQ&usqp=CAc"
    }]
    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]
    return products