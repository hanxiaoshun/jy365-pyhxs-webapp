from orm import Model, CharField, BooleanField, FloatField, TextField, IntegerField, DateTimeField, DecimalField, DateField

class HisAddress(Model):
    id = IntegerField(primary_key=True)
    addresstype = CharField(db_column='addressType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    address = CharField(max_length=100, blank=True, null=True)
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'his_address'


class HisHeight(Model):
    id = IntegerField(primary_key=True)
    height = CharField(max_length=10)
    generationtime = DateField(db_column='generationTime')  # Field name made lowercase.
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    __table__ = 'his_height'


class HisMobile(Model):
    id = IntegerField(primary_key=True)
    mobilenumber = CharField(db_column='mobileNumber', max_length=15, blank=True, null=True)  # Field name made lowercase.
    operator = CharField(max_length=1, blank=True, null=True)
    generationtime = DateTimeField(db_column='generationTime', blank=True, null=True)  # Field name made lowercase.
    disusetime = DateTimeField(db_column='disuseTime', blank=True, null=True)  # Field name made lowercase.
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'his_mobile'


class HisName(Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=20, blank=True, null=True)
    generationtime = DateTimeField(db_column='generationTime', blank=True, null=True)  # Field name made lowercase.
    disusetime = DateTimeField(db_column='disuseTime', blank=True, null=True)  # Field name made lowercase.
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'his_name'


class HisQq(Model):
    id = IntegerField(primary_key=True)
    qq = CharField(max_length=15, blank=True, null=True)
    qqtype = CharField(db_column='qqType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'his_qq'


class HisSina(Model):
    id = IntegerField(primary_key=True)
    sinaaccount = CharField(db_column='sinaAccount', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sinatype = CharField(db_column='sinaType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    generationtime = DateTimeField(db_column='generationTime', blank=True, null=True)  # Field name made lowercase.
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'his_sina'


class HisSleep(Model):
    id = IntegerField(primary_key=True)
    gotobed = DateTimeField(db_column='goToBed', blank=True, null=True)  # Field name made lowercase.
    getup = DateTimeField(db_column='getUp', blank=True, null=True)  # Field name made lowercase.
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'his_sleep'


class HisVersion(Model):
    id = IntegerField(primary_key=True)
    version = CharField(max_length=10)
    generationtime = DateTimeField(db_column='generationTime')  # Field name made lowercase.
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'his_version'


class HisWechat(Model):
    id = IntegerField(primary_key=True)
    wechat = CharField(max_length=20)
    wechattype = CharField(db_column='wechatType', max_length=1)  # Field name made lowercase.
    generationtime = DateTimeField(db_column='generationTime')  # Field name made lowercase.
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'his_wechat'


class HisWeight(Model):
    id = IntegerField(primary_key=True)
    weight = DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    generationtime = DateTimeField(db_column='generationTime', blank=True, null=True)  # Field name made lowercase.
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'his_weight'


class JobColleague(Model):
    id = IntegerField(primary_key=True)
    realname = CharField(db_column='realName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nickname = CharField(max_length=20, blank=True, null=True)
    sex = CharField(max_length=1, blank=True, null=True)
    majormobile = CharField(db_column='majorMobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    majoremail = CharField(db_column='majorEmail', max_length=20, blank=True, null=True)  # Field name made lowercase.
    colleaguetype = CharField(db_column='colleagueType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    majorwork = CharField(db_column='majorWork', max_length=20, blank=True, null=True)  # Field name made lowercase.
    majorposition = CharField(db_column='majorPosition', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nationality = CharField(max_length=15, blank=True, null=True)
    ethnicity = CharField(max_length=15, blank=True, null=True)
    address = CharField(max_length=255, blank=True, null=True)
    highesteducation = CharField(db_column='highestEducation', max_length=1, blank=True, null=True)  # Field name made lowercase.
    evaluate = CharField(max_length=255, blank=True, null=True)
    friendliness = IntegerField(db_column='Friendliness', blank=True, null=True)  # Field name made lowercase.
    birthday = DateField(blank=True, null=True)
    age = IntegerField(blank=True, null=True)
    enterpriceid = IntegerField(db_column='enterpriceId', blank=True, null=True)  # Field name made lowercase.
    postid = IntegerField(db_column='postId', blank=True, null=True)  # Field name made lowercase.
    userid = IntegerField(db_column='userId')  # Field name made lowercase.
    __table__ = 'job_colleague'
    unique_together = (('id', 'userid'),)


class JobEnterprise(Model):
    id = IntegerField(primary_key=True)
    nameofenterprise = CharField(db_column='nameOfEnterprise', max_length=30, blank=True, null=True)  # Field name made lowercase.
    codeofenterprise = CharField(db_column='codeOfEnterprise', max_length=20, blank=True, null=True)  # Field name made lowercase.
    typeofenterprise = CharField(db_column='TypeOfEnterprise', max_length=1, blank=True, null=True)  # Field name made lowercase.
    chairmanofenterprise = CharField(db_column='chairmanOfEnterprise', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ceoofenterprise = CharField(db_column='ceoOfEnterprise', max_length=15, blank=True, null=True)  # Field name made lowercase.
    scaleofenterprise = IntegerField(db_column='scaleOfEnterprise', blank=True, null=True)  # Field name made lowercase.
    addressofenterprise = CharField(db_column='addressOfEnterprise', max_length=100, blank=True, null=True)  # Field name made lowercase.
    genaratetime = DateTimeField(db_column='genarateTime', blank=True, null=True)  # Field name made lowercase.
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'job_enterprise'


class JobInfo(Model):
    id = IntegerField(primary_key=True)
    jobname = CharField(db_column='jobName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    jobtype = CharField(db_column='jobType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    enterpriseid = IntegerField(db_column='enterpriseId')  # Field name made lowercase.
    occupationallevelfirst = IntegerField(db_column='occupationalLevelFirst')  # Field name made lowercase.
    occupationallevelscond = IntegerField(db_column='occupationalLevelScond')  # Field name made lowercase.
    occupationallevelthird = IntegerField(db_column='occupationalLevelThird')  # Field name made lowercase.
    domainclassification = IntegerField(db_column='domainClassification')  # Field name made lowercase.
    jobdescription = CharField(db_column='jobDescription', max_length=255)  # Field name made lowercase.
    evaluate = CharField(max_length=255, blank=True, null=True)
    enterpriceid = IntegerField(db_column='enterpriceId', blank=True, null=True)  # Field name made lowercase.
    postid = IntegerField(db_column='postId', blank=True, null=True)  # Field name made lowercase.
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    genaratetime = DateTimeField(db_column='genarateTime', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'job_info'


class JobPostlevel(Model):
    id = IntegerField(primary_key=True)
    postname = CharField(db_column='postName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    postdescribe = CharField(db_column='postDescribe', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parentid = IntegerField(db_column='parentId', blank=True, null=True)  # Field name made lowercase.
    enterpriseid = IntegerField(db_column='enterpriseId')  # Field name made lowercase.
    generatetime = DateTimeField(db_column='generateTime', blank=True, null=True)  # Field name made lowercase.
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'job_postlevel'
    unique_together = (('id', 'enterpriseid'),)


class JobSalarybenefit(Model):
    id = IntegerField(primary_key=True)
    jobnumber = CharField(db_column='jobNumber', max_length=20, blank=True, null=True)  # Field name made lowercase.
    salarylevel = CharField(db_column='salaryLevel', max_length=1, blank=True, null=True)  # Field name made lowercase.
    salary = DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    endowment = DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    medical = DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    unemployment = DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    jobinjury = DecimalField(db_column='jobInjury', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    maternity = DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    houseingfund = DecimalField(db_column='houseingFund', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    agewage = DecimalField(db_column='ageWage', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bonus = DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    overtimeallowance = DecimalField(db_column='overtimeAllowance', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    deductmoney = DecimalField(db_column='deductMoney', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    cutforleave = DecimalField(db_column='cutForLeave', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    achievement = DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    postallowance = DecimalField(db_column='postAllowance', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    businesstraveallowance = DecimalField(db_column='businessTraveAllowance', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    otherexpenses = DecimalField(db_column='otherExpenses', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    salarynote = CharField(db_column='salaryNote', max_length=255, blank=True, null=True)  # Field name made lowercase.
    enterpriseid = IntegerField(db_column='enterpriseId', blank=True, null=True)  # Field name made lowercase.
    postid = IntegerField(db_column='postId', blank=True, null=True)  # Field name made lowercase.
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'job_salarybenefit'


class ProInfo(Model):
    id = IntegerField(primary_key=True)
    procode = CharField(db_column='proCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    protheme = CharField(db_column='proTheme', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prounits = CharField(db_column='proUnits', max_length=255, blank=True, null=True)  # Field name made lowercase.
    proname = CharField(db_column='proName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    prodomain = CharField(db_column='proDomain', max_length=30, blank=True, null=True)  # Field name made lowercase.
    pronature = CharField(db_column='proNature', max_length=30, blank=True, null=True)  # Field name made lowercase.
    procommander = CharField(db_column='proCommander', max_length=15, blank=True, null=True)  # Field name made lowercase.
    progoal = CharField(db_column='proGoal', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prostatus = CharField(db_column='proStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    proouridentity = CharField(db_column='proOurIdentity', max_length=1, blank=True, null=True)  # Field name made lowercase.
    proexpectation = CharField(db_column='proExpectation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    prostarttime = DateTimeField(db_column='proStartTime', blank=True, null=True)  # Field name made lowercase.
    propreendtime = DateTimeField(db_column='proPreEndTime', blank=True, null=True)  # Field name made lowercase.
    proactuallyendtime = DateTimeField(db_column='proActuallyEndTime', blank=True, null=True)  # Field name made lowercase.
    procase = CharField(db_column='proCase', max_length=255, blank=True, null=True)  # Field name made lowercase.
    resultprediction = CharField(db_column='resultPrediction', max_length=255, blank=True, null=True)  # Field name made lowercase.
    profund = DecimalField(db_column='proFund', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    proriskfund = DecimalField(db_column='proRiskFund', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    pronumber = IntegerField(db_column='proNumber', blank=True, null=True)  # Field name made lowercase.
    promypost = CharField(db_column='proMyPost', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mainenterpriseid = IntegerField(db_column='mainEnterpriseId', blank=True, null=True)  # Field name made lowercase.
    mainschoolid = IntegerField(db_column='mainSchoolId', blank=True, null=True)  # Field name made lowercase.
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'pro_Info'


class ProNode(Model):
    id = IntegerField(primary_key=True)
    nodecode = CharField(db_column='nodeCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nodename = CharField(db_column='nodeName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nodetargettask = CharField(db_column='nodeTargetTask', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nodetype = CharField(db_column='nodeType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    nodeexpectationproduce = CharField(db_column='nodeExpectationProduce', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nodecommander = CharField(db_column='nodeCommander', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nodestarttime = DateTimeField(db_column='nodeStartTime', blank=True, null=True)  # Field name made lowercase.
    nodeendtime = DateTimeField(db_column='nodeEndTime', blank=True, null=True)  # Field name made lowercase.
    nodestatus = CharField(db_column='nodeStatus', max_length=1, blank=True, null=True)  # Field name made lowercase.
    proinfoid = IntegerField(db_column='proInfoId', blank=True, null=True)  # Field name made lowercase.
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'pro_node'


class ProProgress(Model):
    id = IntegerField(primary_key=True)
    progresscode = CharField(db_column='progressCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    progresstitle = CharField(db_column='progressTitle', max_length=30, blank=True, null=True)  # Field name made lowercase.
    progressoutline = CharField(db_column='progressOutline', max_length=255, blank=True, null=True)  # Field name made lowercase.
    progressachievement = CharField(db_column='progressAchievement', max_length=1, blank=True, null=True)  # Field name made lowercase.
    projectid = IntegerField(db_column='projectId', blank=True, null=True)  # Field name made lowercase.
    nodeid = IntegerField(db_column='nodeId', blank=True, null=True)  # Field name made lowercase.
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'pro_progress'


class SchoolClass(Model):
    id = IntegerField(primary_key=True)
    classname = CharField(db_column='className', max_length=10, blank=True, null=True)  # Field name made lowercase.
    classsong = CharField(db_column='classSong', max_length=10, blank=True, null=True)  # Field name made lowercase.
    classdeclaration = CharField(db_column='classDeclaration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    classlable = CharField(db_column='classLable', max_length=255, blank=True, null=True)  # Field name made lowercase.
    classmonitor = CharField(db_column='classMonitor', max_length=15, blank=True, null=True)  # Field name made lowercase.
    term = CharField(max_length=15, blank=True, null=True)
    generatetime = DateTimeField(db_column='generateTime', blank=True, null=True)  # Field name made lowercase.
    schoolid = IntegerField(db_column='schoolId', blank=True, null=True)  # Field name made lowercase.
    teachername = CharField(db_column='teacherName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    teacherid = IntegerField(db_column='teacherId', blank=True, null=True)  # Field name made lowercase.
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'school_class'


class SchoolClassmate(Model):
    id = IntegerField(primary_key=True)
    realname = CharField(db_column='realName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nickname = CharField(max_length=20, blank=True, null=True)
    sex = CharField(max_length=1, blank=True, null=True)
    age = IntegerField(blank=True, null=True)
    majormobile = CharField(db_column='majorMobile', max_length=15, blank=True, null=True)  # Field name made lowercase.
    majoremail = CharField(db_column='majorEmail', max_length=20, blank=True, null=True)  # Field name made lowercase.
    matetype = CharField(db_column='mateType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    birthday = DateField(blank=True, null=True)
    nationality = CharField(max_length=15, blank=True, null=True)
    ethnicity = CharField(max_length=15, blank=True, null=True)
    highesteducation = CharField(db_column='highestEducation', max_length=1, blank=True, null=True)  # Field name made lowercase.
    majorwork = CharField(db_column='majorWork', max_length=20, blank=True, null=True)  # Field name made lowercase.
    majorposition = CharField(db_column='majorPosition', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address = CharField(max_length=255, blank=True, null=True)
    evaluate = CharField(max_length=255, blank=True, null=True)
    friendliness = IntegerField(db_column='Friendliness', blank=True, null=True)  # Field name made lowercase.
    schoolid = IntegerField(db_column='schoolId', blank=True, null=True)  # Field name made lowercase.
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'school_classmate'


class SchoolCourse(Model):
    id = IntegerField(primary_key=True)
    coursename = CharField(db_column='courseName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    courseteacher = CharField(db_column='courseTeacher', max_length=20, blank=True, null=True)  # Field name made lowercase.
    coursecontent = CharField(db_column='courseContent', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coursebook = CharField(db_column='courseBook', max_length=255, blank=True, null=True)  # Field name made lowercase.
    classroom = CharField(max_length=20, blank=True, null=True)
    coursescore = DecimalField(db_column='courseScore', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    term = CharField(max_length=10, blank=True, null=True)
    courseevaluate = CharField(db_column='courseEvaluate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    remark = CharField(max_length=255, blank=True, null=True)
    generationtime = DateTimeField(db_column='generationTime', blank=True, null=True)  # Field name made lowercase.
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'school_course'


class SchoolExamination(Model):
    id = IntegerField(primary_key=True)
    subject = CharField(max_length=20, blank=True, null=True)
    examtype = CharField(db_column='examType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    examexplain = CharField(db_column='examExplain', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invigilator = CharField(max_length=20, blank=True, null=True)
    score = DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    term = CharField(max_length=10, blank=True, null=True)
    evaluate = CharField(max_length=255, blank=True, null=True)
    teacherid = IntegerField(db_column='teacherId', blank=True, null=True)  # Field name made lowercase.
    courseid = IntegerField(db_column='courseId', blank=True, null=True)  # Field name made lowercase.
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'school_examination'


class SchoolInfo(Model):
    id = IntegerField(primary_key=True)
    schoolname = CharField(db_column='schoolName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    schooltype = CharField(db_column='schoolType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    schooladdress = CharField(db_column='schoolAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    collegetype = CharField(db_column='collegeType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    collegename = CharField(db_column='collegeName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    major = CharField(max_length=30, blank=True, null=True)
    majortype = CharField(db_column='majorType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    grade = IntegerField(blank=True, null=True)
    class_field = IntegerField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    generationtime = DateTimeField(db_column='generationTime', blank=True, null=True)  # Field name made lowercase.
    remark = CharField(max_length=255, blank=True, null=True)
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'school_info'


class SchoolTeacher(Model):
    id = IntegerField(primary_key=True)
    teachername = CharField(db_column='teacherName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    sex = CharField(max_length=1, blank=True, null=True)
    term = CharField(max_length=10, blank=True, null=True)
    teacherlevel = CharField(db_column='teacherLevel', max_length=1, blank=True, null=True)  # Field name made lowercase.
    teachertype = CharField(db_column='teacherType', max_length=1, blank=True, null=True)  # Field name made lowercase.
    evaluate = CharField(max_length=255, blank=True, null=True)
    generationtime = DateTimeField(db_column='generationTime', blank=True, null=True)  # Field name made lowercase.
    schoolid = IntegerField(db_column='schoolId', blank=True, null=True)  # Field name made lowercase.
    courseid = IntegerField(db_column='courseId', blank=True, null=True)  # Field name made lowercase.
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'school_teacher'


class UsMenuinfo(Model):
    id = IntegerField(primary_key=True)
    menuname = CharField(db_column='menuName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    __table__ = 'us_menuinfo'


class UsRoleinfo(Model):
    id = IntegerField(primary_key=True)
    rolename = CharField(db_column='roleName', max_length=20, blank=True, null=True)  # Field name made lowercase.

    __table__ = 'us_roleinfo'


class UsRolemenu(Model):
    id = IntegerField(primary_key=True)
    roleid = IntegerField(db_column='roleId', blank=True, null=True)  # Field name made lowercase.
    menuid = IntegerField(db_column='menuId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'us_rolemenu'


class UsUserinfo(Model):
    id = IntegerField(primary_key=True)
    useraccount = CharField(db_column='userAccount', max_length=30)  # Field name made lowercase.
    userrealname = CharField(db_column='userRealName', max_length=50)  # Field name made lowercase.
    usercurrentpwd = CharField(db_column='userCurrentPwd', max_length=50)  # Field name made lowercase.
    usercurrentnickname = CharField(db_column='userCurrentNickname', max_length=20)  # Field name made lowercase.
    usercurrentsex = IntegerField(db_column='userCurrentSex', blank=True, null=True)  # Field name made lowercase.
    age = IntegerField(blank=True, null=True)
    usercurrentmajormobile = CharField(db_column='userCurrentMajorMobile', max_length=30, blank=True, null=True)  # Field name made lowercase.
    usercurrentmajoremail = CharField(db_column='userCurrentMajorEmail', max_length=30, blank=True, null=True)  # Field name made lowercase.
    birthday = DateField(blank=True, null=True)
    usercurrentnationality = CharField(db_column='userCurrentNationality', max_length=15, blank=True, null=True)  # Field name made lowercase.
    usercurrentethnicity = CharField(db_column='userCurrentEthnicity', max_length=15, blank=True, null=True)  # Field name made lowercase.
    usercurrenthighesteducation = CharField(db_column='userCurrentHighestEducation', max_length=10, blank=True, null=True)  # Field name made lowercase.
    usercurrentmajorwork = CharField(db_column='userCurrentMajorWork', max_length=20, blank=True, null=True)  # Field name made lowercase.
    usercurrentposition = CharField(db_column='userCurrentPosition', max_length=20, blank=True, null=True)  # Field name made lowercase.
    usercurrentmajoraddress = CharField(db_column='userCurrentMajorAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    usercurrentmajorwechat = CharField(db_column='userCurrentMajorWeChat', max_length=30, blank=True, null=True)  # Field name made lowercase.
    usercurrentmajorqq = CharField(db_column='userCurrentMajorQQ', max_length=30, blank=True, null=True)  # Field name made lowercase.
    usercurrentmajorsinablog = CharField(db_column='userCurrentMajorSinaBlog', max_length=30, blank=True, null=True)  # Field name made lowercase.
    usercurrentweight = DecimalField(db_column='userCurrentWeight', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    usercurrentheight = DecimalField(db_column='userCurrentHeight', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    usercurrentsgb = IntegerField(db_column='userCurrentSGB', blank=True, null=True)  # Field name made lowercase.
    generationtime = DateTimeField(db_column='generationTime', blank=True, null=True)  # Field name made lowercase.
    modificationtime = DateTimeField(db_column='modificationTime', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'us_userinfo'


class UsUserrole(Model):
    id = IntegerField(primary_key=True)
    userid = IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.
    roleid = IntegerField(db_column='roleId', blank=True, null=True)  # Field name made lowercase.

    __table__ = 'us_userrole'
