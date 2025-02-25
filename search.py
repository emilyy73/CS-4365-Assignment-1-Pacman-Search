# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from typing import List
from game import Directions
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    sucessor_ds = util.Stack()
    actions = []
    
    visited = util.Counter()
    
    sucessor_ds.push((problem.getStartState(), Directions.SOUTH, -1))

    while (not util.Stack.isEmpty(sucessor_ds)):
        current_triple = sucessor_ds.pop()
        
        if (problem.isGoalState(current_triple[0])):
            actions.append(current_triple)
            actions_dirs = []
            for action in actions:
                actions_dirs.append(action[1])
            return actions_dirs
        elif visited[current_triple[0]] > 0:
            continue
        
        visited[current_triple[0]] = 1 # only add the node to set
        if current_triple[2] != -1:
            actions.append(current_triple)
        
        successors = problem.getSuccessors(current_triple[0])
        
        branches = 0
        for successor in successors:
            if visited[successor[0]] > 0:
                continue
            branches += 1
            sucessor_ds.push(successor)
                        
        # backtrace
        if branches == 0:
            keep_tracing = True
            while(keep_tracing):
                back = actions.pop()
                back_s = problem.getSuccessors(back[0])
                for option in back_s:
                    if visited[option[0]] == 0:
                        keep_tracing = False
                        actions.append(back) # recover last action 
                        
        pass
    
    return []
    
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    sucessor_ds = util.Queue()
    
    visited = {}
    parentMap = {problem.getStartState() : ((-1, -1), Directions.EAST, -1)}
    
    sucessor_ds.push((problem.getStartState(), Directions.SOUTH, -1))


    while (not util.Queue.isEmpty(sucessor_ds)):
        current_triple = sucessor_ds.pop()
        
        
        # backtrace
        if (problem.isGoalState(current_triple[0])):
            end = current_triple
            actions = []
            
            # while we havent backtraced to start
            while(end[0] != problem.getStartState()):
                actions.append(end[1])
                end = parentMap[end[0]]
            rev = reversed(actions)
            
            return list(rev)
        
        successors = problem.getSuccessors(current_triple[0])
        
        for successor in successors:
            # if we visited then it has a parent
            if successor[0] in parentMap:
                continue
            parentMap[successor[0]] = current_triple
            sucessor_ds.push(successor)
                        
        pass
    
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
