from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg, LeggedRobotCfgPPO

class Z1Cfg( LeggedRobotCfg ):
    class init_state( LeggedRobotCfg.init_state ):
        pos = [0.0, 0.0, 0.5] # x,y,z [m]
        # [0, 1, 0, 1] 对应绕 Y 轴旋转 90 度，使机器人面朝下趴在地上
        rot = [0.0, 1.0, 0.0, 1.0] # x,y,z,w [quat]
        
        # 严格对应 Z1 URDF 的 23 个自由度
        target_joint_angles = { 
           # 髋部顺序：Pitch -> Roll -> Yaw [cite: 8, 12, 16]
           'left_hip_pitch_joint' : -0.1,         
           'left_hip_roll_joint' : 0.0,               
           'left_hip_yaw_joint' : 0.0,   
           'left_knee_joint' : 0.3,       
           'left_ankle_pitch_joint' : -0.2,     
           'left_ankle_roll_joint' : 0.0,
           
           'right_hip_pitch_joint' : -0.1,                                       
           'right_hip_roll_joint' : 0.0, 
           'right_hip_yaw_joint' : 0.0, 
           'right_knee_joint' : 0.3,                                             
           'right_ankle_pitch_joint': -0.2,                              
           'right_ankle_roll_joint' : 0.0,     
           
           'waist_yaw_joint' : 0.0, 
           
           'left_shoulder_pitch_joint' : 0.0,
           'left_shoulder_roll_joint' : 0.3, 
           'left_shoulder_yaw_joint' : 0.0,
           'left_elbow_joint' : 0.0,
           'left_wrist_yaw_joint' : 0.0, # Z1 腕部为 yaw 轴 [cite: 80]
           
           'right_shoulder_pitch_joint' : 0.0,
           'right_shoulder_roll_joint' : -0.3,
           'right_shoulder_yaw_joint' : 0.0,
           'right_elbow_joint' : 0.0,
           'right_wrist_yaw_joint' : 0.0,
        }

        default_joint_angles = { 
           'left_hip_pitch_joint' : -0.1,         
           'left_hip_roll_joint' : 0.0,               
           'left_hip_yaw_joint' : 0.0,   
           'left_knee_joint' : 0.3,       
           'left_ankle_pitch_joint' : -0.2,     
           'left_ankle_roll_joint' : 0.0,     
           
           'right_hip_pitch_joint' : -0.1,                                       
           'right_hip_roll_joint' : 0.0, 
           'right_hip_yaw_joint' : 0.0, 
           'right_knee_joint' : 0.3,                                             
           'right_ankle_pitch_joint': -0.2,                              
           'right_ankle_roll_joint' : 0.0,       
           
           'waist_yaw_joint' : 0.0, 
           
           'left_shoulder_pitch_joint' : 0.0,
           'left_shoulder_roll_joint' : 0.0,
           'left_shoulder_yaw_joint' : 0.0,
           'left_elbow_joint' : 0.8,
           'left_wrist_yaw_joint' : 0.0,    
           
           'right_shoulder_pitch_joint' : 0.0,
           'right_shoulder_roll_joint' : 0.0,
           'right_shoulder_yaw_joint' : 0.0,
           'right_elbow_joint' : 0.8,
           'right_wrist_yaw_joint' : 0.0,
        }

    class env(LeggedRobotCfg.env):
        num_one_step_observations = 76 
        num_actions = 23 # 修正为实际 DOF 数量
        num_dofs = 23
        num_actor_history = 6
        num_observations = num_actor_history * num_one_step_observations
        episode_length_s = 10 
        unactuated_timesteps = 30

    class control( LeggedRobotCfg.control ):
        control_type = 'P'
        # 针对 Z1 更大的重量，适当提升了膝盖和髋部的刚度
        stiffness = {'hip': 180,  # G1 原本为 150
                     'knee': 240, # G1 原本为 200
                     'ankle': 40,
                     'shoulder': 100,
                     'elbow': 100,
                     'waist': 100,
                     'wrist': 100,
                     } 
        damping = {  'hip': 5,
                     'knee': 8,
                     'ankle': 2,
                     'shoulder': 4,
                     'elbow': 4,
                     'waist': 4,
                     'wrist': 4,
                     } 
        action_scale = 1
        decimation = 4

    class asset( LeggedRobotCfg.asset ):
        file = '{LEGGED_GYM_ROOT_DIR}/resources/robots/z1/MagicBotZ1_23dof.urdf'
        name = "z1"
        left_foot_name = "left_foot"
        right_foot_name = "right_foot"
        left_knee_name = 'left_knee'
        right_knee_name = 'right_knee'
        left_thigh_name = 'left_hip_pitch'
        right_thigh_name = 'right_hip_pitch'
        foot_name = "foot"
        penalize_contacts_on = ["elbow", 'shoulder', 'waist', 'knee', 'hip']
        terminate_after_contacts_on = [] 
        self_collisions = 0 
        flip_visual_attachments = False

        # 按照 Z1 的物理拓扑顺序重排：Pitch -> Roll -> Yaw
        left_leg_joints = ['left_hip_pitch_joint', 'left_hip_roll_joint', 'left_hip_yaw_joint', 'left_knee_joint', 'left_ankle_pitch_joint', 'left_ankle_roll_joint']
        right_leg_joints = ['right_hip_pitch_joint', 'right_hip_roll_joint', 'right_hip_yaw_joint', 'right_knee_joint', 'right_ankle_pitch_joint', 'right_ankle_roll_joint']
        
        left_arm_joints = ['left_shoulder_pitch_joint', 'left_shoulder_roll_joint', 'left_shoulder_yaw_joint', 'left_elbow_joint', 'left_wrist_yaw_joint']
        right_arm_joints = ['right_shoulder_pitch_joint', 'right_shoulder_roll_joint', 'right_shoulder_yaw_joint', 'right_elbow_joint', 'right_wrist_yaw_joint']
        
        waist_joints = ["waist_yaw_joint"]
        knee_joints = ['left_knee_joint', 'right_knee_joint']
        ankle_joints = [ 'left_ankle_pitch_joint', 'left_ankle_roll_joint', 'right_ankle_pitch_joint', 'right_ankle_roll_joint']

        # 核心修正：Z1 的 Base 是 pelvis，而非 torso [cite: 1, 60]
        trunk_names = ["pelvis", "torso_link"]
        base_name = 'pelvis' 
        tracking_body_names =  ['pelvis']

    class rewards( LeggedRobotCfg.rewards ):
        soft_dof_pos_limit = 0.9
        soft_dof_vel_limit = 0.9
        # Z1 站立高度约 0.8m，这里设定目标高度为 0.8
        base_height_target = 0.8
        base_height_sigma = 0.25
        target_base_height_phase1 = 0.45
        target_base_height_phase2 = 0.45
        target_base_height_phase3 = 0.70
        
        reward_groups = ['task', 'regu', 'style', 'target']
        num_reward_groups = len(reward_groups)
        reward_group_weights = [1, 0.1, 1, 1]

        class scales:
            task_orientation = 1
            task_head_height = 1

    class constraints( LeggedRobotCfg.rewards ):
        # 继承 G1 的约束逻辑
        is_gaussian = True
        target_base_height = 0.45
        post_task = False
        
        class scales:
            regu_dof_acc = -2.5e-7
            regu_action_rate = -0.01
            regu_smoothness = -0.01 
            regu_torques = -2.5e-6
            regu_joint_power = -2.5e-5
            regu_dof_vel = -1e-3
            regu_dof_pos_limits = -100.0

            style_waist_deviation = -10
            style_hip_yaw_deviation = -10
            style_hip_roll_deviation = -10
            style_hip_pitch_deviation = -10
            style_shoulder_roll_deviation = -2.5
            style_thigh_ori = 10
            style_feet_distance = -10

            target_ang_vel_xy = 10
            target_lin_vel_xy = 10
            target_target_orientation = 10
            target_target_base_height = 10

    class curriculum:
        # 保留“上帝之手”拉力辅助初始化
        pull_force = True
        force = 100 
        threshold_height = 0.9

    class sim(LeggedRobotCfg.sim):
        dt = 0.005
        substeps = 1
        up_axis = 1  # 1 is Z axis

class Z1CfgPPO( LeggedRobotCfgPPO ):
    class runner( LeggedRobotCfgPPO.runner ):
        run_name = ''
        experiment_name = 'z1_ground_prone'
        max_iterations = 12000