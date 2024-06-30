from llama_index.core.tools import FunctionTool

def optimize_portfolio(expected_returns, covariances, risk_tolerance):
    """Optimizes portfolio allocation based on inputs.

    Args:
        expected_returns (pd.Series or np.ndarray): Expected returns for each asset.
        covariances (pd.DataFrame or np.ndarray): Covariance matrix of asset returns.
        risk_tolerance (float): Investor's risk tolerance (higher value means more risk aversion).

    Returns:
        pd.Series: Optimal weights for each asset in the portfolio.
    """

    n = len(expected_returns)

    # Convert to numpy arrays if pandas Series/DataFrame are provided
    if isinstance(expected_returns, pd.Series):
        expected_returns = expected_returns.values
    if isinstance(covariances, pd.DataFrame):
        covariances = covariances.values

    w = cp.Variable(n)
    ret = expected_returns.T @ w 
    risk = cp.quad_form(w, covariances)
    target_return = cp.Parameter(nonneg=True)

    constraints = [cp.sum(w) == 1, w >= 0, ret >= target_return]

    prob = cp.Problem(cp.Maximize(ret - risk_tolerance * risk), constraints)

    target_return.value = 0  # Start with minimum return
    prob.solve()

    # Convert numpy array back to pandas Series with asset names as index
    if isinstance(expected_returns, pd.Series):
        optimal_weights = pd.Series(w.value, index=expected_returns.index)
    else:
        optimal_weights = pd.Series(w.value)

    return optimal_weights


portfolio_optimization_tool = FunctionTool.from_defaults(
    optimize_portfolio,
    name="PortfolioOptimizationTool",
    description="Optimize portfolio allocation based on expected returns, covariances, and risk tolerance."
)
