from effort2.formfactors.formFactorBtoC import FormFactorBToDstar


class BToDStarCLN(FormFactorBToDstar):

    def __init__(
        self,
        m_B: float,
        m_V: float,
        h_A1_1: float,
        rho2: float,
        R1_1: float, 
        R2_1: float,
        m_L: float = 0,
        R0_1: float = 0, 
        ):
        """[summary]

        Args:
            m_B (float): [description]
            m_M (float): [description]
            h_A1_1 (float, optional): [description]
            rho2 (float, optional): [description]
            R1_1 (float, optional): [description]
            R2_1 (float, optional): [description]
        """
        super().__init__(m_B, m_V, m_L)
        self.h_A1_1 = h_A1_1
        self.rho2 = rho2
        self.R0_1 = R0_1
        self.R1_1 = R1_1
        self.R2_1 = R2_1


    def h_A1(self, w: float) -> float:
        """[summary]

        Args:
            w (float): [description]

        Returns:
            float: [description]
        """
        rho2 = self.rho2
        z = self.z(w)
        return self.h_A1_1 * (1 - 8 * rho2 * z + (53 * rho2 - 15) * z ** 2 - (231 * rho2 - 91) * z ** 3)


    def R0(self, w) -> None:
        """From https://arxiv.org/pdf/1203.2654.pdf

        Returns:
            _type_: _description_
        """
        return self.R0_1 - 0.11 * (w - 1) + 0.01 * (w - 1) ** 2


    def R1(self, w: float) -> float:
        """[summary]

        Args:
            w (float): [description]

        Returns:
            float: [description]
        """
        return self.R1_1 - 0.12 * (w - 1) + 0.05 * (w - 1) ** 2


    def R2(self, w: float) -> float:
        """[summary]

        Args:
            w (float): [description]

        Returns:
            float: [description]
        """
        return self.R2_1 + 0.11 * (w - 1) - 0.06 * (w - 1) ** 2


