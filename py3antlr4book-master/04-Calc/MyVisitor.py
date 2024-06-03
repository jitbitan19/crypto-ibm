__author__ = "jszheng"

from LabeledExprVisitor import LabeledExprVisitor
from LabeledExprParser import LabeledExprParser


class MyVisitor(LabeledExprVisitor):
    def __init__(self):
        self.memory = {}

    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        # return 0

    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value
        print(f"{name} <-- {value}")
        # return value

    def visitInt(self, ctx):
        return ctx.INT().getText()

    def visitId(self, ctx):
        name = ctx.ID().getText()
        if name in self.memory:
            return self.memory[name]
        return 0

    # def visitMulDiv(self, ctx):
    #     left = int(self.visit(ctx.expr(0)))
    #     right = int(self.visit(ctx.expr(1)))
    #     if ctx.op.type == LabeledExprParser.MUL:
    #         return left * right
    #     return left / right

    # def visitAddSub(self, ctx):
    #     left = int(self.visit(ctx.expr(0)))
    #     right = int(self.visit(ctx.expr(1)))
    #     if ctx.op.type == LabeledExprParser.ADD:
    #         return left + right
    #     return left - right

    # def visitOperation(self, ctx: LabeledExprParser.OperationContext):
    #     # return super().visitOperation(ctx)
    #     l = int(self.visit(ctx.expr(0)))
    #     r = int(self.visit(ctx.expr(1)))

    #     if ctx.OP().getText() == "*":
    #         return l * r
    #     elif ctx.OP().getText() == "/":
    #         return l / r
    #     elif ctx.OP().getText() == "+":
    #         return l + r
    #     else:
    #         return l - r

    def visitOp1(self, ctx: LabeledExprParser.Op1Context):
        # return super().visitOp1(ctx)
        l = int(self.visit(ctx.expr(0)))
        r = int(self.visit(ctx.expr(1)))
        if ctx.MULDIV().getText() == "*":
            return l * r
        return l / r

    def visitOp2(self, ctx: LabeledExprParser.Op2Context):
        # return super().visitOp2(ctx)
        l = int(self.visit(ctx.expr(0)))
        r = int(self.visit(ctx.expr(1)))
        if ctx.ADDSUB().getText() == "+":
            return l + r
        return l - r

    def visitParens(self, ctx):
        return self.visit(ctx.expr())
