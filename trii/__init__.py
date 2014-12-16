

class DecisionTree():
    def __init__(self, evaluator, *children):
        """
        * evaluator: a function that returns something. On evaluation, this
            will be passed to self.result.
        * children: the child decision trees of this decision tree.
            A child is a tuple of (condition, result).
            A condition is either a value (evaluated for equality), or a
                predicate.
            A result is either a DecisionTree, a function, or a value.
        """
        self.evaluator = evaluator
        self.children = set(children)
        self.value = None

    def add_child(self, *args):
        args = (args[0], args[1]) if len(args) >= 2 else args
        self.children.add(args)

    def evaluate(self, env):
        """Given the environment, evaluate."""
        evalulator_args = {k: v for k, v in env.items()}
        result = self.evaluator(**evalulator_args)
        self.value = result

    def decide(self, env):
        """Given the environment, make a decision."""
        self.evaluate(env)
        for condition, result in self.children:
            if ((callable(condition) and condition(self.value))
                    or (self.value == condition)):
                if isinstance(result, DecisionTree):
                    return result.decide(env)
                elif callable(result):
                    return result()
                else:
                    return result
